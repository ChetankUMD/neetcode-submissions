"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if intervals == []:
            return True
        intervals.sort(key=lambda x: (x.start, x.end))
        output = []
        output.append(intervals[0])
        print(output)
        for i in range(1,len(intervals)):
            lastend = output[-1].end
            print(lastend)
            if intervals[i].start < lastend:
                return False
            else:
                output.append(intervals[i])
        return True