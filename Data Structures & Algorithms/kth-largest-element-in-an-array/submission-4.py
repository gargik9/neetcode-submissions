class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        nums = [-n for n in nums]
        heapq.heapify(nums)

        c = 0
        while c < k-1:
            heapq.heappop(nums)
            c+=1
        return -nums[0]


        