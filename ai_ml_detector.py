import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
from sklearn.ensemble import IsolationForest
from sklearn.linear_model import LinearRegression

# Read counts data
try:
    df = pd.read_csv('counts.csv', names=['ip', 'count'])
except FileNotFoundError:
    print("❌ ERROR: counts.csv not found. Run insider_detector.py first.")
    exit(1)

# Create output folder
output_folder = 'plots'
os.makedirs(output_folder, exist_ok=True)

for ip, group in df.groupby('ip'):
    counts = group['count'].values
    sample_numbers = np.arange(1, len(counts) + 1).reshape(-1, 1)

    if len(counts) < 5:
        print(f"[INFO] {ip}: Not enough data (only {len(counts)} samples). Skipping...")
        continue

    # ML model
    model = IsolationForest(contamination=0.01, random_state=42)
    model.fit(counts.reshape(-1, 1))
    preds = model.predict(counts.reshape(-1, 1))

    # Calculate mean and std
    mean = np.mean(counts)
    std = np.std(counts)

    # Fit trend line
    linreg = LinearRegression()
    linreg.fit(sample_numbers, counts)
    trend = linreg.predict(sample_numbers)

    # Plot
    plt.figure(figsize=(12, 6))
    plt.plot(sample_numbers, counts, marker='o', label='Event Count', color='blue')
    plt.plot(sample_numbers, trend, label='Trend Line', linestyle='--', color='purple')

    anomalies = np.where(preds == -1)[0]
    if len(anomalies) > 0:
        plt.scatter(sample_numbers[anomalies], counts[anomalies], color='red', label='Anomalies', s=100, edgecolors='black')

    # Mean line
    plt.axhline(mean, color='green', linestyle='-', linewidth=1.5, label='Mean')

    # Std deviation band
    plt.fill_between(sample_numbers.flatten(), mean - std, mean + std, color='yellow', alpha=0.2, label='±1 Std Dev')

    # Labels & styling
    plt.title(f"Detailed Event Analysis for {ip}", fontsize=16)
    plt.xlabel("Sample Number", fontsize=12)
    plt.ylabel("Event Count", fontsize=12)
    plt.legend()
    plt.grid(True)
    plt.tight_layout()

    plot_path = f"{output_folder}/{ip.replace('.', '_')}_detailed.png"
    plt.savefig(plot_path)
    plt.close()
    print(f"[PLOT SAVED] {plot_path}")

