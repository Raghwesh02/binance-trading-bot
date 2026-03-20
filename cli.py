import argparse

from bot.client import get_client
from bot.orders import place_order
from bot.validators import validate_order
from bot.logging_config import setup_logger


def main():
    setup_logger()

    parser = argparse.ArgumentParser(description="Binance Futures Trading Bot")

    parser.add_argument("--symbol", required=True)
    parser.add_argument("--side", required=True)
    parser.add_argument("--type", required=True)
    parser.add_argument("--quantity", type=float, required=True)
    parser.add_argument("--price", type=float)

    args = parser.parse_args()

    try:
        # Validate input
        validate_order(
            args.symbol,
            args.side,
            args.type,
            args.quantity,
            args.price
        )

        client = get_client()

        print("\n📌 Order Summary:")
        print(vars(args))

        order = place_order(
            client,
            args.symbol,
            args.side,
            args.type,
            args.quantity,
            args.price
        )

        print("\n✅ Order Response:")

        if order:
            print({
                "orderId": order.get("orderId"),
                "status": order.get("status"),
                "executedQty": order.get("executedQty"),
                "avgPrice": order.get("avgPrice")
            })
        else:
            print("⚠️ No response received")

    except Exception as e:
        print(f"\n❌ Error: {str(e)}")


if __name__ == "__main__":
    main()