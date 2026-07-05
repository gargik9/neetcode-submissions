"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        intervals.sort(key=lambda i:i.start)
        if intervals:
            last = intervals[0] 
    

        for current in intervals[1:]:

            if current.start<last.end:
                return False

            last = current

        return True



   