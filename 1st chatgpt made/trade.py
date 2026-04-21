from typing import Dict, List
from datamodel import Order, OrderDepth, TradingState
from strategy_utils import get_mid_price


class Trader:

    POSITION_LIMIT = 20
    SPREAD = 2

    def run(self, state: TradingState) -> Dict[str, List[Order]]:

        result = {}

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

        return result