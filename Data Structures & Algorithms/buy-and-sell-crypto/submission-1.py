class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # so looking at this, what we are returning is a max profit
        # so we need to be tracking a min day and a current profit and get the max of a profit
        # so  we are going to be implementing a two pointer solution to keep track of our variables
        # so we cannot sort the array, prices are tied to indices (day)
        left = 0
        maxProfit = 0
        for i in range(1,len(prices)):
            if prices[left] > prices[i]:
                prices[left] = prices[i] 
            profit = prices[i] - prices[left]
            maxProfit = max(profit, maxProfit)
        return maxProfit