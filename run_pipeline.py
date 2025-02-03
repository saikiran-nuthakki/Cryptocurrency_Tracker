from fetch_data import fetch_coin_universe, fetch_coin_prices
from analyze_data import analyze_vs_bitcoin
from compute_historical_difference import compute_avg_change
import time
import sys



"""
This script runs a pipeline to fetch cryptocurrency data, analyze it, and compute historical averages.
Steps in the pipeline:
1. Fetch the universe of coins (Coins + Metadata)
2. Fetch price data for tracked coins (Specified Coin Data)
3. Analyze the relationship with Bitcoin (Coin Price vs Bitcoin Price over 24h)
4. Compute historical averages of Coins in relationship with Bitcoin (Over previous runs)
"""



steps = [
    ("Step #1: Fetching the universe of coins (Coins + Metadata)", fetch_coin_universe),
    ("Step #2: Fetching price data for tracked coins (Specified Coin Data)", fetch_coin_prices),
    ("Step #3: Analyzing the relationship with Bitcoin (Coin Price vs Bitcoin Price)", analyze_vs_bitcoin),
    ("Step #4: Computing historical averages", compute_avg_change)
]


for step_description, step_function in steps:
    print(step_description)
    sys.stdout.flush()  # Ensure step name is printed before execution
    start_time = time.time()
    
    if step_function == fetch_coin_prices:
        pricing_file = step_function()
    elif step_function == analyze_vs_bitcoin:
        step_function(pricing_file)
    else:
        step_function()
    
    elapsed_time = time.time() - start_time
    print(f"Completed in {elapsed_time:.2f} seconds\n")
