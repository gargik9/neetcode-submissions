class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        currSum = 0
        res = 0
        hashmap = {0:1}

        for num in nums:

            currSum += num

            if (currSum - k) in hashmap:

                res+= hashmap[currSum-k]

            hashmap[currSum] = hashmap.get(currSum, 0) + 1

        return res
