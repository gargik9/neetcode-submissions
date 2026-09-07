class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort()
        res = [intervals[0]]

        prevStart = intervals[0][0]
        prevEnd = intervals[0][1]

        for start, end in intervals[1:]:

            if start <= prevEnd:
                prevEnd = max(prevEnd, end)
                res[-1] = [prevStart, prevEnd]

            else:
                res.append([start, end])
                prevStart = start
                prevEnd = end

        return res

        



            


        


