class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        mini = prices[0]
        max_diff = float('-inf')
        curr_diff = 0

        for num in prices:

            if num<mini:
                mini = num

            curr_diff = num - mini 

            if curr_diff>max_diff:

                max_diff = curr_diff

        return max_diff