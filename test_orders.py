from bot.client import get_client
from bot.orders import place_order

client = get_client()

try:
    order = place_order(
        client,
        symbol="BTCUSDT",
        side="BUY",
        order_type="MARKET",
        quantity=0.001
    )

    print("✅ Order placed successfully!")
    print(order)

except Exception as e:
    print("❌ Error:", str(e))