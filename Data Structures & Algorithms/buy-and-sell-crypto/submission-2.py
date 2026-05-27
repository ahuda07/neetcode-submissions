class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # so looking at this, what we are returning is a max profit
        # so we need to be tracking a min price to buy and a current profit and get the max of a profit
        # so  we are going to be implementing a two pointer solution to keep track of our variables
        # so we cannot sort the array, prices are tied to indices (day)
        min_prices = prices[0]
        maxProfit = 0
        for price in prices:
            if min_prices > price:
                min_prices = price
            profit = price - min_prices
            maxProfit = max(profit, maxProfit)
        return maxProfit

        # after doing solution
        # i realized that we need to check if current price is greater than the current iteration, then we can get a new buying price
        # then we can calculate a profit given a new buy price