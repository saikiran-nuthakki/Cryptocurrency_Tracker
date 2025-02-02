import pandas as pd
import os
from config import DATA_DIR


"""
Computes the average 24-hour percent change across all historical runs.

This function reads all CSV files in the DATA_DIR directory that start with "btc_relationship_".
It concatenates these files into a single DataFrame, computes the average 24-hour percent change
for each cryptocurrency symbol relative to Bitcoin, and saves the result to a CSV file named
"avg_24h_change_vs_btc.csv" in the DATA_DIR directory.
"""

def compute_avg_change():
    
    files = [f for f in os.listdir(DATA_DIR) if f.startswith("btc_relationship_")]
    
    # Read all pricing data files
    df_list = [pd.read_csv(f"{DATA_DIR}/{f}") for f in files]
    df_all = pd.concat(df_list)
    
    # Compute averages
    avg_changes = df_all.groupby("symbol")["24h_diff_vs_btc"].mean().reset_index()
    avg_changes.to_csv(f"{DATA_DIR}/avg_24h_change_vs_btc.csv", index=False)
