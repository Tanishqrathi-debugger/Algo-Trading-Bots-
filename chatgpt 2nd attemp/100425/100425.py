from typing import Dict, List


class Order:
    def __init__(self, product: str, price: int, quantity: int):
        self.product = product
        self.price = price
        self.quantity = quantity

    def __repr__(self):
        return f"Order({self.product}, {self.price}, {self.quantity})"


class OrderDepth:
    def __init__(self):
        self.buy_orders: Dict[int, int] = {}
        self.sell_orders: Dict[int, int] = {}


class TradingState:
    def __init__(self, timestamp, order_depths, position, traderData=""):
        self.timestamp = timestamp
        self.order_depths = order_depths
        self.position = position
        self.traderData = traderData


def get_mid_price(order_depth: OrderDepth):

    if len(order_depth.buy_orders) == 0 or len(order_depth.sell_orders) == 0:
        return None

    best_bid = max(order_depth.buy_orders.keys())
    best_ask = min(order_depth.sell_orders.keys())

    return (best_bid + best_ask) / 2


class Trader:

    POSITION_LIMIT = 20
    SPREAD = 2

    def run(self, state: TradingState):

        result: Dict[str, List[Order]] = {}
        conversions = 0
        traderData = ""

        for product in state.order_depths:

            order_depth: OrderDepth = state.order_depths[product]
            orders: List[Order] = []

            position = state.position.get(product, 0)

            mid_price = get_mid_price(order_depth)

            if mid_price is None:
                result[product] = []
                continue

            buy_price = int(mid_price - self.SPREAD)
            sell_price = int(mid_price + self.SPREAD)

            if position < self.POSITION_LIMIT:
                orders.append(Order(product, buy_price, 5))

            if position > -self.POSITION_LIMIT:
                orders.append(Order(product, sell_price, -5))

            result[product] = orders

        return result, conversions, traderData