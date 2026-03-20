# Binance Futures Testnet Trading Bot

A modular Python-based trading bot for Binance Futures Testnet (USDT-M) that supports order placement via CLI and a lightweight Streamlit UI.

---

## 🚀 Features

- Place MARKET and LIMIT orders
- Supports both BUY and SELL sides
- CLI interface using argparse
- Lightweight UI using Streamlit
- Input validation and error handling
- Structured logging of API requests and responses
- Handles real exchange constraints:
  - Minimum notional value
  - Tick size
  - Price precision
  - Timestamp synchronization

---

## 🛠️ Tech Stack

- Python 3.x
- python-binance
- Streamlit
- argparse
- logging

---

## ⚙️ Setup Instructions

1. Clone the repository:

git clone https://github.com/Raghwesh02/binance-trading-bot.git  
cd binance-trading-bot

2. Install dependencies:

pip install -r requirements.txt

3. Create a `.env` file:

API_KEY=your_api_key  
API_SECRET=your_api_secret  

---

## ▶️ Usage

### 🔹 CLI (Command Line)

#### Market Order:
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.002

#### Limit Order (Manual Price):
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.002 --price 70000

#### Limit Order (Auto Price):
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.002

---

### 🔹 UI (Streamlit)

Run:

python -m streamlit run ui.py

This provides an interactive interface for placing orders.

---

## 📊 Logging

All API activity and errors are logged in:

trading_bot.log

Includes:
- Order requests
- API responses
- Errors and exceptions

---

## 📁 Project Structure

binance-trading-bot/
│
├── bot/
│   ├── __init__.py
│   ├── client.py
│   ├── orders.py
│   ├── validators.py
│   ├── logging_config.py
│
├── cli.py
├── ui.py
├── requirements.txt
├── README.md
├── trading_bot.log

---

## ⚠️ Assumptions

- Uses Binance Futures Testnet (USDT-M)
- Minimum order value ≥ 100 USDT
- Price must follow tick size and precision rules
- `.env` file is required for API credentials

---

## 🧠 Challenges & Solutions

- Timestamp Errors → Fixed using server time synchronization  
- Empty API Responses → Handled via order polling  
- Tick Size & Precision Issues → Implemented price normalization  
- Limit Price Restrictions → Added dynamic price fetching  

---

## 📌 Future Improvements

- WebSocket integration for live price updates  
- Strategy-based auto trading  
- Risk management (stop-loss, take-profit)  
- Portfolio tracking dashboard  

---

## 📧 Author

Raghwesh Rathour
