import sys
import os
import pandas as pd

# Ensure the project root is in sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from fetch_data import fetch_coin_universe  # Now import should work

def test_fetch_coin_universe():
    """Ensures that the fetch_coin_universe function generates a valid CSV file."""
    fetch_coin_universe()
    df = pd.read_csv("crypto_data/coin_universe.csv")
    assert not df.empty
