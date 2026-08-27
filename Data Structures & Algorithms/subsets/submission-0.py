class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        res = [[]]

        for num in nums:

            new = [subset + [num] for subset in res]
            res+= new

        
        return res

        
        