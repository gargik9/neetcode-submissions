class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        total = 0
        range_sum = 0
        for num in nums:
            total+= num 

        for i in range(len(nums)+1):
            range_sum+=i

        missing_number = range_sum - total

        return missing_number