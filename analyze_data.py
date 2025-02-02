import os
import pandas as pd
from config import DATA_DIR

"""
This function reads a CSV file containing cryptocurrency pricing data, calculates the 
absolute difference in 24-hour percentage change between each cryptocurrency and Bitcoin, 
and saves the analysis to a new CSV file.
Args:
    pricing_file (str): The filename of the CSV file containing the cryptocurrency pricing data.
Returns:
    None
"""


def analyze_vs_bitcoin(pricing_file):
    
    #Ensures the pricing file path is correct before reading
    file_path = os.path.join(DATA_DIR, os.path.basename(pricing_file))  # Fix path handling
    print(f"Reading file: {file_path}")  # Debugging line

    df = pd.read_csv(file_path)  # Read the correct file

    btc_change = df[df["symbol"] == "BTC"]["percent_change_24h"].values[0]
    df["diff_vs_btc"] = abs(df["percent_change_24h"] - btc_change)
    df = df[df["symbol"] != "BTC"].sort_values("diff_vs_btc")

    df = df.drop(columns=["price","percent_change_24h","cmc_rank", "IsTopCurrency"])
    analysis_file = os.path.join(DATA_DIR, f"btc_relationship_{os.path.basename(pricing_file)}")
    df.to_csv(analysis_file, index=False)
    print(f"Saved analysis: {analysis_file}")  