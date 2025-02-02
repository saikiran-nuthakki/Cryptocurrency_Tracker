import requests
import pandas as pd
import logging
from datetime import datetime
from config import BASE_URL, HEADERS, DATA_DIR

"""
This file provides functions to fetch and save cryptocurrency data.
Functions:
    fetch_coin_universe(): Fetches the entire universe of coins and saves them as a CSV.
    load_coins_to_track(): Loads the list of coins to track from coins_to_track.csv.
    fetch_coin_prices(): Fetches real-time price data for tracked coins and saves them as a CSV.
"""

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Fetches the entire universe of coins and saves them as a CSV
def fetch_coin_universe():
    url = f"{BASE_URL}cryptocurrency/listings/latest"
    try:
        response = requests.get(url, headers=HEADERS)
        response.raise_for_status()
        data = response.json()
        
        if "data" not in data:
            logging.error(f"Unexpected response format: {data}")
            return

        df = pd.DataFrame([
            {"id": c["id"], "name": c["name"], "symbol": c["symbol"], "cmc_rank": c["cmc_rank"]}
            for c in data["data"]
        ])
        df.to_csv(f"{DATA_DIR}/coin_universe.csv", index=False)
        logging.info("Successfully fetched and saved coin universe.")
    except requests.RequestException as e:
        logging.error(f"Error fetching coin universe: {e}", exc_info=True)
        return


# Loads the list of coins to track from coins_to_track.csv
def load_coins_to_track():
    try:
        df = pd.read_csv("coins_to_track.csv")
        logging.info("Successfully loaded coins to track.")
        return df["symbol"].tolist()
    except FileNotFoundError:
        logging.error("coins_to_track.csv not found.", exc_info=True)
        return []
    except pd.errors.EmptyDataError:
        logging.error("coins_to_track.csv is empty.", exc_info=True)
        return []


# Fetches real-time price data for tracked coins
def fetch_coin_prices():
    """Fetches real-time price data for tracked coins."""
    symbols = load_coins_to_track()
    if not symbols:
        logging.error("No coins to track. Check coins_to_track.csv.")
        return

    url = f"{BASE_URL}cryptocurrency/quotes/latest?symbol={','.join(symbols)}"
    try:
        response = requests.get(url, headers=HEADERS)
        response.raise_for_status()
        data = response.json()
        
        if "data" not in data:
            logging.error(f"Unexpected response format: {data}")
            return

        records = []
        for symbol in symbols:
            if symbol in data["data"]:
                coin_data = data["data"][symbol]
                cmc_rank = coin_data.get("cmc_rank", float("inf"))  # Default to inf if missing
                is_top_currency = cmc_rank <= 10  # Correct boolean check
                
                records.append({
                    "symbol": symbol,
                    "price": coin_data["quote"]["USD"]["price"],
                    "percent_change_24h": coin_data["quote"]["USD"]["percent_change_24h"],
                    "cmc_rank": cmc_rank,
                    "IsTopCurrency": is_top_currency,
                    "LoadedWhen": datetime.now()
                })

        filename = f"{DATA_DIR}/crypto_prices_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
        pd.DataFrame(records).to_csv(filename, index=False)
        logging.info(f"Successfully fetched and saved coin prices to {filename}.")
        return filename
    except requests.RequestException as e:
        logging.error(f"Error fetching coin prices: {e}", exc_info=True)
        return
