import logging
import time
import math

def format_price(price, tick_size=0.1):
    # Remove floating error + enforce tick size
    price = math.floor(price / tick_size) * tick_size
    return float(f"{price:.1f}")  # 🔥 force 1 decimal place

def place_order(client, symbol, side, order_type, quantity, price=None):

    try:
        logging.info(f"Placing order: {symbol}, {side}, {order_type}, {quantity}, {price}")

        # Ensure one-way mode
        try:
            client.futures_change_position_mode(dualSidePosition=False)
        except Exception:
            pass

        # ======================
        # MARKET ORDER
        # ======================
        if order_type == "MARKET":
            order = client.futures_create_order(
                symbol=symbol,
                side=side,
                type="MARKET",
                quantity=quantity
            )

        # ======================
        # LIMIT ORDER
        # ======================
        elif order_type == "LIMIT":

            # Auto-fetch price
            if price is None:
                price_data = client.futures_mark_price(symbol=symbol)
                price = float(price_data['markPrice'])

                if side == "BUY":
                    price *= 0.999
                else:
                    price *= 1.001

            # 🔥 FIX EVERYTHING HERE
            price = format_price(price)

            print(f"📊 Final valid price: {price}")

            order = client.futures_create_order(
                symbol=symbol,
                side=side,
                type="LIMIT",
                quantity=quantity,
                price=str(price),
                timeInForce="GTC"
            )

        else:
            raise ValueError("Invalid order type")

        logging.info(f"Initial response: {order}")

        time.sleep(2)

        orders = client.futures_get_all_orders(symbol=symbol)

        if not orders:
            return order

        latest_order = orders[-1]

        logging.info(f"Final order: {latest_order}")
        return latest_order

    except Exception as e:
        logging.error(f"Order failed: {str(e)}")
        raise