# Binance Futures Testnet Trading Bot

## Setup

1. Clone the repository

2. Install dependencies:
pip install -r requirements.txt

3. Create .env file:
API_KEY=your_key
API_SECRET=your_secret

## Run

### Market Order
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.002

### Limit Order
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.002 --price 60000

## Optional UI (Streamlit)

You can also run the bot using a simple UI:

```bash
python -m streamlit run ui.py

## Features

- Market & Limit Orders
- CLI input support
- Input validation
- Logging system
- Error handling
- Binance Futures Testnet integration

## Assumptions

- Using USDT-M Futures
- Minimum order value ≥ 100 USDT