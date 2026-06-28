class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        min_heap = []

        hashmap = {}

        res = []

        for num in nums:

           hashmap[num] = hashmap.get(num,0)+1

        for num in hashmap:
            freq = hashmap[num]

            heapq.heappush(min_heap,(freq,num))

            if len(min_heap)>k:
                heapq.heappop(min_heap)

        for i in range(k):

            res.append(heapq.heappop(min_heap)[1])

        return res
