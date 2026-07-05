class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        heapq.heapify_max(stones)
        max_heap = stones
        ans = 0

        while len(max_heap)>1:
            num1 = heapq.heappop_max(max_heap)
            num2 = heapq.heappop_max(max_heap)
            diff = num1 - num2
            heapq.heappush_max(max_heap,diff)

        ans = heapq.heappop_max(max_heap)

        return ans

        
        
            