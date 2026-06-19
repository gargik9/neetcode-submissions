class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        min_heap = []

        map = {}

        for num in nums:
            map[num] = map.get(num,0)+1

        for num,freq in map.items():

            heapq.heappush(min_heap, (freq,num))

        while len(min_heap)>k:
            heapq.heappop(min_heap)

        res = []

        for i in range(k):

            res.append(heapq.heappop(min_heap)[1])

        return res


