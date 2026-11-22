class Solution:
    def trap(self, height: List[int]) -> int:
        
        left = 0
        right = len(height)-1
        res=0

        leftMax=height[left]
        rightMax=height[right]

        while left<right:

            if leftMax<=rightMax:
                left+=1
                leftMax= max(height[left],leftMax)
                res+=leftMax-height[left]

            else:
                right-=1
                rightMax = max(height[right],rightMax)
                res+=rightMax-height[right]

        return res







        