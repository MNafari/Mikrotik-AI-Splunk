# Identifying Disgruntled Employee Behavior in Cybersecurity Teams Using Mikrotik, AI & Splunk

## Project Name

**Mikrotik-AI-Splunk**

---

## ⚠ Disclaimer

* All IP addresses and employee names used in this project are **fictional** and meant only for demonstration.
* This project is intended for educational and research purposes only.

---

## 📊 Overview

This experimental project showcases how to detect suspicious or abnormal employee behavior within a cybersecurity team using:

* **Mikrotik Router** for collecting network traffic logs.
* **TP-Link Switch** for network distribution.
* **Splunk Enterprise** for log indexing and searching.
* **Python scripts** with integrated AI/ML models to analyze employee behaviors in real time.

### Key Use Case

The main idea is to monitor internal network activities (such as repeated pings, abnormal traffic patterns) and identify employees who may be acting outside normal behavior patterns, potentially indicating dissatisfaction or insider threats.

---

## 🛡️ Network Architecture

![Network Diagram](photo/diagram-network.png)

* Internet ⮕ Mikrotik Router ⮕ TP-Link Switch ⮕ Employees' PCs

### Employee PCs (Example)

| Name | IP Address     |
| ---- | -------------- |
| Alex | 192.168.10.100 |
| Sara | 192.168.10.105 |
| Mike | 192.168.10.112 |
| John | 192.168.10.117 |
| Emma | 192.168.10.94  |

> For detailed diagrams, check the `photo/` folder.

---

## 🔧 Tools & Technologies

* **Mikrotik Router**: Sending syslog events to Splunk.
* **TP-Link Switch**: Connecting employee devices.
* **Splunk Enterprise**: Collecting, indexing, and searching network logs.
* **Python Scripts**:

  * `insider_detector.py`: Real-time log monitoring.
  * `ai_ml_detector.py`: Advanced ML-based behavior analysis and plotting.

> Sample screenshots are available in the `photo/` folder.

---

## 🛠️ Setup Steps

1. **Configure Splunk**

   * Navigate to **Settings > Data Inputs > UDP**.
   * Set up a UDP listener for Mikrotik syslog (e.g., port 10514).

2. **Configure Mikrotik Router**

   * Set logging rules to forward to Splunk server IP and port.

3. **Run Python Scripts**

   * Start `insider_detector.py` for live monitoring.
   * Run `ai_ml_detector.py` to apply ML models and generate plots.

4. **Review Outputs**

   * Console alerts for detected anomalies.
   * Graphical plots saved in `plots/` directory.

---

## 👁️ AI/ML Integration

The `ai_ml_detector.py` script uses simple machine learning algorithms to:

* Track event counts per IP.
* Apply trend analysis, moving averages, and standard deviation checks.
* Highlight anomalies visually.

Example Output Plot:

![Final Analysis](photo/final-analysis.png)

> Note: With more data and integration, this framework can evolve into more advanced models like Isolation Forest or LSTM for time-series anomaly detection.

---

## 📈 Real-World Potential

* Monitor insider threats in corporate environments.
* Provide early warnings for potentially dissatisfied employees.
* Expand to cover richer behaviors (file access, login times, web activity).

---

## 🛠️ Future Improvements

* Deploy more sophisticated anomaly detection algorithms.
* Integrate alert systems (e.g., Slack, email, dashboards).
* Automate remediation (e.g., temporarily isolate suspicious devices).
* Build a proper frontend for SOC teams to visualize results.

---

## 📧 Contact

M. Nafari
Email: **[m.nafarai@gmail.com](mailto:m.nafarai@gmail.com)**

For all detailed visuals, screenshots, and diagrams, check the repository's `photo/` branch or folder.

---

This README is designed to provide clear, structured, and professional documentation to help others understand the value, setup, and potential of this project.

