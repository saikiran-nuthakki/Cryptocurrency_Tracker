import os

# CoinMarketCap API Key (Use an environment variable for security)
API_KEY = os.getenv("CMC_API_KEY", "b438220a-b349-4742-81d3-d6d8b2339057")

# CoinMarketCap API Base URL
BASE_URL = "https://pro-api.coinmarketcap.com/v1/"

# Headers for API requests
HEADERS = {"X-CMC_PRO_API_KEY": API_KEY}

# Data storage directory
DATA_DIR = "crypto_data"
os.makedirs(DATA_DIR, exist_ok=True)
