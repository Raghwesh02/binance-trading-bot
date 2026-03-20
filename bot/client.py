import os
import time
from binance.client import Client
from dotenv import load_dotenv

load_dotenv()

def get_client():
    api_key = os.getenv("API_KEY")
    api_secret = os.getenv("API_SECRET")

    if not api_key or not api_secret:
        raise Exception("API keys not found")

    client = Client(api_key, api_secret, testnet=True)

    # Correct futures testnet URL
    client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"

    # 🔥 TIME SYNC FIX
    server_time = client.get_server_time()
    system_time = int(time.time() * 1000)
    offset = server_time['serverTime'] - system_time

    client.timestamp_offset = offset

    return client