class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        max_total = float('-inf')
        curr_total = 0

        for num in nums:

            if curr_total<0:

                curr_total = 0

            curr_total = num + curr_total

            max_total = max(max_total,curr_total)

        return max_total


