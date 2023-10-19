class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # not valid prices array
        if not prices:
            return 0

        # keep track of the maximum profit as we iterate
        max_profit = 0

        # array to keep track of the minimum value from prices[0:i]
        min_prices = [prices[0]]

        # iterate
        for price in prices[1:]:
            # update max profit
            latest_min_price = min_prices[-1]
            max_profit = max(max_profit, price - latest_min_price)

            # get current minimum price and append
            min_prices.append(min(price, min_prices[-1]))
            

        return max_profit

            