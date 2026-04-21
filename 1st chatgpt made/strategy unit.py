def get_mid_price(order_depth):

    if not order_depth.buy_orders or not order_depth.sell_orders:
        return None

    best_bid = max(order_depth.buy_orders.keys())
    best_ask = min(order_depth.sell_orders.keys())

    return (best_bid + best_ask) / 2


def position_limit_check(position, limit):

    if position > limit:
        return "SELL"

    if position < -limit:
        return "BUY"

    return "OK"