class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        max_total = float('-inf')
        curr_total = 0

        for num in nums:

            curr_total+=num
            if curr_total<num:
                curr_total=num
            max_total = max(curr_total,max_total)

        return max_total


