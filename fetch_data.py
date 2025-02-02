import requests
import pandas as pd
from datetime import datetime
from config import BASE_URL, HEADERS, DATA_DIR

def fetch_coin_universe():
    """Fetches the entire universe of coins and saves them as a CSV."""
    url = f"{BASE_URL}cryptocurrency/listings/latest"
    response = requests.get(url, headers=HEADERS).json()
    
    if "data" not in response:
        print(f"Error fetching data: {response}")
        return

    df = pd.DataFrame([
        {"id": c["id"], "name": c["name"], "symbol": c["symbol"], "cmc_rank": c["cmc_rank"]}
        for c in response["data"]
    ])
    df.to_csv(f"{DATA_DIR}/coin_universe.csv", index=False)

def load_coins_to_track():
    """Loads the list of coins to track from coins_to_track.csv."""
    return pd.read_csv("coins_to_track.csv")["symbol"].tolist()

def fetch_coin_prices():
    """Fetches real-time price data for tracked coins."""
    symbols = load_coins_to_track()
    url = f"{BASE_URL}cryptocurrency/quotes/latest?symbol={','.join(symbols)}"
    response = requests.get(url, headers=HEADERS).json()
    
    if "data" not in response:
        print(f"Error fetching pricing data: {response}")
        return

    records = [
        {
            "symbol": symbol,
            "price": response["data"][symbol]["quote"]["USD"]["price"],
            "percent_change_24h": response["data"][symbol]["quote"]["USD"]["percent_change_24h"],
            "LoadedWhen": datetime.now()
        }
        for symbol in symbols if symbol in response["data"]
    ]

    filename = f"{DATA_DIR}/crypto_prices_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
    pd.DataFrame(records).to_csv(filename, index=False)
    return filename
