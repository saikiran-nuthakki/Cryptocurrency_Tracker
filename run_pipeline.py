from fetch_data import fetch_coin_universe, fetch_coin_prices
from analyze_data import analyze_vs_bitcoin
from compute_metrics import compute_avg_change
import time
import sys

# Define the steps in the pipeline
steps = [
    ("Step #1: Fetching the universe of coins...", fetch_coin_universe),
    ("Step #2: Fetching price data for tracked coins...", fetch_coin_prices),
    ("Step #3: Analyzing the relationship with Bitcoin...", analyze_vs_bitcoin),
    ("Step #4: Computing historical averages...", compute_avg_change)
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
