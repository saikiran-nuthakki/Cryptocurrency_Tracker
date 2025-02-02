import pandas as pd
import os
from config import DATA_DIR

def compute_avg_change():
    """Computes the average 24-hour percent change across all historical runs."""
    files = [f for f in os.listdir(DATA_DIR) if f.startswith("crypto_prices_")]
    
    # Read all pricing data files
    df_list = [pd.read_csv(f"{DATA_DIR}/{f}") for f in files]
    df_all = pd.concat(df_list)
    
    # Compute averages
    avg_changes = df_all.groupby("symbol")["percent_change_24h"].mean().reset_index()
    avg_changes.to_csv(f"{DATA_DIR}/avg_24h_change_vs_btc.csv", index=False)
