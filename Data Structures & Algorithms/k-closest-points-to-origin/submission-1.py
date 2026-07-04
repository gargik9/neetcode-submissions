class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        min_heap = []
        res = []

        for p in points:
            distance = math.sqrt(p[0]*p[0] + p[1]*p[1])

            heapq.heappush(min_heap,(distance,p))

        for _ in range(k):
            res.append(heapq.heappop(min_heap)[1])

        return res

        