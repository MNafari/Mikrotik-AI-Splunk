import csv
import json
import time
import re
from collections import defaultdict
from splunklib.client import Service
from splunklib.results import JSONResultsReader

# Load config
with open('configs/splunk_config.json') as config_file:
    config = json.load(config_file)

# Splunk config
splunk_host = config['splunk']['host']
splunk_port = config['splunk']['port']
splunk_username = config['splunk']['username']
splunk_password = config['splunk']['password']
search_query = config['splunk']['query']

# AI config
THRESHOLD = config['ai']['threshold']

# Regex for extracting IP addresses
ip_pattern = re.compile(r'(192\.168\.10\.\d{1,3})')

# Load employee list
employees = {}
with open('employees.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        employees[row['ip']] = {'name': row['name'], 'email': row['email']}

# Connect to Splunk
print("Starting continuous monitoring...")
service = Service(
    host=splunk_host,
    port=splunk_port,
    username=splunk_username,
    password=splunk_password,
    scheme='https',
    app='search'
)

try:
    service.login()
    print("✅ SUCCESS: Connected to Splunk!")

    while True:
        print("🔄 Running new check...")
        kwargs_search = {"exec_mode": "blocking", "output_mode": "json"}
        job = service.jobs.create(search_query, **kwargs_search)

        # Count suspicious events per IP
        event_counts = defaultdict(int)
        found_any = False

        for result in JSONResultsReader(job.results(output_mode='json')):
            if isinstance(result, dict):
                raw_event = result.get('_raw', '')
                found_ips = ip_pattern.findall(raw_event)
                for ip in found_ips:
                    if ip != '192.168.10.1':
                        event_counts[ip] += 1
                        found_any = True

        # Save counts to file
        with open('counts.csv', 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            for ip, count in event_counts.items():
                writer.writerow([ip, count])

        # Print alerts
        if found_any:
            for ip, count in event_counts.items():
                if ip in employees and count > THRESHOLD:
                    name = employees[ip]['name']
                    print(f"[ALERT] {name} ({ip}) exceeded threshold with {count} events.")
        else:
            print("✅ No suspicious events detected.")

        print("⏳ Waiting 30 second before next check...")
        time.sleep(30)  # Wait for 5 minutes

except Exception as e:
    print(f"❌ ERROR: {e}")

