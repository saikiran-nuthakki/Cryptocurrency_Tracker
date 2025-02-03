# Cryptocurrency Tracker

This project is a cryptocurrency tracker that fetches real-time price data from the CoinMarketCap API, analyzes price movements against Bitcoin, and computes historical trends. It supports tracking multiple cryptocurrencies dynamically from a configuration file and outputs analysis results in CSV format.

## Features
- **Fetches real-time cryptocurrency prices** using the CoinMarketCap API.
- **Tracks multiple cryptocurrencies dynamically** based on `coins_to_track.csv`.
- **Analyzes price movement relative to Bitcoin** and sorts by absolute difference.
- **Computes historical 24H percent change trends** over multiple runs.
- **Built with Python and Pipenv for environment management.**

## Setup & Installation
### 1. Clone the Repository
```sh
git clone https://github.com/yourusername/Cryptocurrency_Tracker.git
cd Cryptocurrency_Tracker
```

### 2. Install Dependencies
Ensure you have **Python 3.9+** installed, then set up the environment:
```sh
python -m pip install --user pipenv
python -m pipenv install --dev
```

### 3. Add Your API Key
CoinMarketCap requires an API key. Update `config.py` and replace "your_coinmarketcap_api_key" with API key:
```python
API_KEY = os.getenv("CMC_API_KEY", "your_coinmarketcap_api_key")
```

### 4. Configure Tracked Coins
Edit `coins_to_track.csv` to specify which cryptocurrencies to track:
```csv
symbol
BTC
ETH
ADA
XRP
DOGE
```

## Running the Tracker
### One-time execution:
```sh
python -m pipenv run python run_pipeline.py
```

## Output & Data
All results are stored in the `crypto_data/` directory:
- **`coin_universe.csv`** → Data for all available coins and their metadata.
- **`crypto_prices_YYYYMMDD_HHMMSS.csv`** → Pricing data for coins from coins_to_track.csv with load datetime, and currency ranking.
- **`btc_relationship_YYYYMMDD_HHMMSS.csv`** → Difference in 24H percent change between bitcoin and the coin being evaluated, sorted in ascending order.
- **`avg_24h_change_vs_btc.csv`** → average 24H percent change vs bitcoin for each currency utilizing the historical 'btc_relationship_YYYYMMDD_HHMMSS.csv' files generated.



### Running Tests
```sh
python -m pipenv run pytest tests/
```

## Roadmap / Future Improvements
- **Database Integration**: Store results in DB of choice.
- **Web Dashboard**: Visualize trends using Streamlit or Flask.
- **Automated Alerts**: Send email/SMS alerts for significant price changes.
- **Historical Backtesting**: Analyze past performance for better insights.


## Author
Saikiran Nuthakki – Data Engineer

---