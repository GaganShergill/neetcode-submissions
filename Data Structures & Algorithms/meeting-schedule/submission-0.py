"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda x: x.start)
        endIdx = None
        for interval in intervals:
            if endIdx and endIdx > interval.start:
                return False
            
            endIdx = interval.end
        
        return True