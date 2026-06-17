class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        max_profit = 0

        min_value = float('inf')

        for i in range(len(prices)):

            profit = prices[i] - min_value

            if prices[i]<min_value:
                min_value = prices[i]

            max_profit = max(profit, max_profit)

        return max_profit


        
        
