from fetch_data import fetch_coin_universe, fetch_coin_prices
from analyze_data import analyze_vs_bitcoin
from compute_metrics import compute_avg_change

# Step 1: Fetch the universe of coins
fetch_coin_universe()

# Step 2: Fetch price data for tracked coins
pricing_file = fetch_coin_prices()

# Step 3: Analyze the relationship with Bitcoin
analyze_vs_bitcoin(pricing_file)

# Step 4: Compute historical averages
compute_avg_change()
