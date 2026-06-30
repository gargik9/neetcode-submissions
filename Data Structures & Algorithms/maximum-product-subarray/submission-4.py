class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
       
        min_so_far = 1
        max_so_far = 1
        res = nums[0]

        for num in nums:

            curr = num

            if num<0:
                min_so_far, max_so_far = max_so_far, min_so_far

            min_so_far = min(curr, curr*min_so_far)
            max_so_far = max(curr, curr*max_so_far)

            res = max(res, max_so_far)

        return res
    

    
