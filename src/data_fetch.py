from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("FINNHUB_API_KEY")
if not api_key:
    raise ValueError("Finnhub api key not found in .env")

