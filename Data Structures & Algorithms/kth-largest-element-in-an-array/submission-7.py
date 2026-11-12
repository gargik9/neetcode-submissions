class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        heapq.heapify(nums)

        i=0
        ans = 0

        for i in range(len(nums)-k+1):
            ans = heapq.heappop(nums)
            

        return ans

    