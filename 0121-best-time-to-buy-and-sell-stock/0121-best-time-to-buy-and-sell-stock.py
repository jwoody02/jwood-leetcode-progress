class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # not valid prices array
        if not prices:
            return 0

        # keep track of the maximum profit as we iterate
        max_profit = 0

        # min price found
        min_price = max(prices)

        # iterate
        for price in prices:
            # update max profit
            max_profit = max(max_profit, price - min_price)

            # get current minimum price and append
            min_price = min(price, min_price)
            

        return max_profit

            