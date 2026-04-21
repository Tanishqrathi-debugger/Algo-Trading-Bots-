from typing import Dict, List
from datamodel import Order, OrderDepth, TradingState


class Trader:

    POSITION_LIMIT = 20
    FAIR_PRICE = 10000

    def run(self, state: TradingState):

        result: Dict[str, List[Order]] = {}
        conversions = 0
        traderData = ""

        for product in state.order_depths:

            order_depth: OrderDepth = state.order_depths[product]
            orders: List[Order] = []

            position = state.position.get(product, 0)

            # BUY LOGIC
            if len(order_depth.sell_orders) > 0:

                best_ask = min(order_depth.sell_orders.keys())
                best_ask_volume = order_depth.sell_orders[best_ask]

                if best_ask < self.FAIR_PRICE and position < self.POSITION_LIMIT:

                    buy_qty = min(-best_ask_volume, self.POSITION_LIMIT - position)

                    orders.append(Order(product, best_ask, buy_qty))

                    print("BUY", product, best_ask, buy_qty)

            # SELL LOGIC
            if len(order_depth.buy_orders) > 0:

                best_bid = max(order_depth.buy_orders.keys())
                best_bid_volume = order_depth.buy_orders[best_bid]

                if best_bid > self.FAIR_PRICE and position > -self.POSITION_LIMIT:

                    sell_qty = min(best_bid_volume, self.POSITION_LIMIT + position)

                    orders.append(Order(product, best_bid, -sell_qty))

                    print("SELL", product, best_bid, sell_qty)

            result[product] = orders

        return result, conversions, traderData