class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        numset = set(nums)

        length = 1
        max_length = 0

        for num in numset:

            length = 1

            while num+length in numset:

                length+=1

            max_length = max(length, max_length)

        return max_length





    