from dotenv import load_dotenv
import os
import requests
import pandas as pd
import yfinance as yf
from datetime import datetime

load_dotenv()
api_key = os.getenv("FINNHUB_API_KEY")

# Fetching data from finnhub API endpoints for stock profiles.
def fetch_finnhub_data(ticker="AAPL"):

    # If no API key, we can just fall back to yahoo finance.
    if not api_key:
        print("No Finnhub API key in .env, falling back to yfinance.")
        stock_data = yf.download(ticker, start="2024-01-01", end="2025-08-02")
        return pd.data({
            "ticker": [ticker],
            "name": [ticker],
            "current_price": [stock_data["Close"].iloc[-1]],
            "industry": ["Unknown"]
        })
    
    # Otherwise if we do have an API key we can fetch its data.
    profile_url = profile_url = f"https://finnhub.io/api/v1/stock/profile2?symbol={ticker}&token={api_key}"
    profile = requests.get(profile_url).json()

    
    