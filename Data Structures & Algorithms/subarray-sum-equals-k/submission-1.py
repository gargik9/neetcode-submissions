class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        prefixSum = {0:1}
        currSum = 0
        ans = 0

        for num in nums:

            currSum+= num
            diff = currSum - k

            ans+= prefixSum.get(diff,0)

            prefixSum[currSum] = prefixSum.get(currSum,0)+1


        return ans




            
        