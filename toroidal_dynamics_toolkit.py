import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from psi_filter_v2 import PsiFilter

def run_multi_shot_benchmark(data_folder, shot_ids, risk_column='disruption_risk'):
    results = []
    for sid in shot_ids:
        df = pd.read_csv(f"{data_folder}/east_shot_{sid}.txt", sep=r'\s+', header=None, names=['time_s', 'ip_ma', risk_column])
        t = df['time_s'].values
        signal = df['ip_ma'].values.astype(float)
        
        # Add real plasma effects
        np.random.seed(42)
        noise = np.random.normal(0, 0.03, len(t))
        spikes = np.random.choice([0, 1], len(t), p=[0.98, 0.02]) * np.random.normal(0, 0.4, len(t))
        wall_drift = 0.02 * np.cumsum(np.random.normal(0, 0.01, len(t)))
        delayed_signal = np.roll(signal + noise + spikes + wall_drift, 2)
        
        features_scaled = (delayed_signal.reshape(-1, 1) - delayed_signal.mean()) / delayed_signal.std()
        
        psi = PsiFilter().reduce(PsiFilter().evolve(features_scaled, t))
        psi_std = np.std(psi)
        risk_corr = np.corrcoef(psi, df[risk_column])[0, 1] if risk_column in df.columns else np.nan
        
        results.append({'shot_id': sid, 'psi_stability': round(psi_std, 3), 'risk_correlation': round(risk_corr, 3)})
    
    summary = pd.DataFrame(results)
    print("\n=== TDT Multi-Shot Summary ===")
    print(summary)
    summary.to_csv("tdt_results.csv", index=False)
    return summary
