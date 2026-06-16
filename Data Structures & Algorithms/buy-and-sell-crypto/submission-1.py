class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        curr_min = float('inf')
        res = 0 

        for price in prices:

            diff = price - curr_min
            res = max(res,diff)

            if price < curr_min:
                curr_min = price

        return res



        
        
