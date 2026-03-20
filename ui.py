import streamlit as st

from bot.client import get_client
from bot.orders import place_order

st.title("📈 Binance Futures Trading Bot")

symbol = st.text_input("Symbol", "BTCUSDT")
side = st.selectbox("Side", ["BUY", "SELL"])
order_type = st.selectbox("Order Type", ["MARKET", "LIMIT"])
quantity = st.number_input("Quantity", min_value=0.001, value=0.002)

price = None
if order_type == "LIMIT":
    price = st.number_input("Price (optional)", value=70000.0)

if st.button("Place Order"):

    try:
        client = get_client()

        order = place_order(
            client,
            symbol,
            side,
            order_type,
            quantity,
            price
        )

        st.success("✅ Order Placed Successfully!")

        if order:
            st.json({
                "orderId": order.get("orderId"),
                "status": order.get("status"),
                "executedQty": order.get("executedQty"),
                "avgPrice": order.get("avgPrice")
            })
        else:
            st.warning("No response received")

    except Exception as e:
        st.error(f"Error: {str(e)}")