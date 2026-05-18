class Solution {
    /**
     * @param {number[]} prices
     * @return {number}
     */
    maxProfit(prices) {
        let maxProfit = 0;
        let minPrice = prices[0];
        for(const price of prices){
            if(price < minPrice){
                minPrice = price;
            }
            let profit = price - minPrice;
            maxProfit = Math.max(maxProfit, profit);
            }
            return maxProfit;
        }
}
