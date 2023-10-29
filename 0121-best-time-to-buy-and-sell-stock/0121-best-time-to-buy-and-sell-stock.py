class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # not valid prices array
        if not prices:
            return 0

        # keep track of the maximum profit as we iterate
        max_profit = 0

        # array to keep track of the minimum value from prices[0:i]
        min_price = float('inf')

        # iterate
        for price in prices:
            # update max profit
            max_profit = max(max_profit, price - min_price)

            # get current minimum price
            min_price = min(price, min_price)
            

        return max_profit

            