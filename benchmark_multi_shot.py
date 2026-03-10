"""
benchmark_multi_shot.py
Toroidal Dynamics Toolkit (TDT) v1.0 - Benchmark Runner
Run this file to test Psi v2 on your real EAST #41195 data
"""

import numpy as np
import pandas as pd
from psi_filter_v2 import PsiFilter   # ← must be in the same folder

print("=== TDT Benchmark - Real EAST #41195 ===")

# Load your existing east_ip.txt file
df = pd.read_csv('east_ip.txt', sep=r'\s+', header=None, names=['time_s', 'ip_ma'])
print(f"Loaded {len(df)} time points from real EAST #41195 discharge")

t = df['time_s'].values
signal = df['ip_ma'].values.astype(float)

# Add realistic plasma effects (noise + wall drift + actuator delay)
np.random.seed(42)
noise = np.random.normal(0, 0.03, len(t))
spikes = np.random.choice([0, 1], len(t), p=[0.98, 0.02]) * np.random.normal(0, 0.4, len(t))
wall_drift = 0.02 * np.cumsum(np.random.normal(0, 0.01, len(t)))

delayed_signal = np.roll(signal + noise + spikes + wall_drift, 2)
delayed_signal[:2] = signal[:2]   # keep start clean

features_scaled = (delayed_signal.reshape(-1, 1) - delayed_signal.mean()) / delayed_signal.std()

# Run Psi v2
psi_filter = PsiFilter(gamma=0.35, attraction_strength=0.8)
psi_output = psi_filter.reduce(psi_filter.evolve(features_scaled, t))
psi_std = np.std(psi_output)

print(f"\nPsi Universe v2 stability on REAL EAST #41195: {psi_std:.3f}")

# Save results
results = pd.DataFrame({
    'shot_id': [41195],
    'psi_stability': [round(psi_std, 3)],
    'data_type': ['Real EAST experimental discharge'],
    'notes': ['With diagnostic noise + wall drift + actuator delay']
})

results.to_csv('tdt_east41195_results.csv', index=False)
print("\nResults saved to: tdt_east41195_results.csv")
print("Ready to add more shots in future versions.")
