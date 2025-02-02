import pytest
import pandas as pd
from fetch_data import fetch_coin_universe

def test_fetch_coin_universe():
    """Ensures that the fetch_coin_universe function generates a valid CSV file."""
    fetch_coin_universe()
    df = pd.read_csv("crypto_data/coin_universe.csv")
    assert not df.empty
