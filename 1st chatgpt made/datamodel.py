from typing import Dict, List


class Order:

    def __init__(self, product: str, price: int, quantity: int):
        self.product = product
        self.price = price
        self.quantity = quantity

    def __repr__(self):
        return f"Order(product={self.product}, price={self.price}, quantity={self.quantity})"


class OrderDepth:

    def __init__(self):
        self.buy_orders: Dict[int, int] = {}
        self.sell_orders: Dict[int, int] = {}


class TradingState:

    def __init__(self, timestamp, order_depths, position):
        self.timestamp = timestamp
        self.order_depths = order_depths
        self.position = position