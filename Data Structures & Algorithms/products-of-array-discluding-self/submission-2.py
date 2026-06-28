class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        left_pro = 1
        right_pro = 1
        res = [1]*len(nums)
        
        for i in range(len(nums)):

            res[i]=left_pro
            left_pro*=nums[i]
            
            

        for j in range(len(nums)-1,-1,-1):
            
            res[j]*=right_pro
            right_pro*=nums[j]
            

        return res

