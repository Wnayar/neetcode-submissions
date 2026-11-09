"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    # tc: O(nlogn), where n is the number of intervals
    # sc: O(1)
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # if no intervals return true 
        if len(intervals) == 0:
            return True 

        # sort intervals in place by starting time 
        intervals.sort(key = lambda x : x.start)

        # go through intervals looking for conflicts, return false if found
        current_start, current_end = intervals[0].start, intervals[0].end 
        for i in range(1, len(intervals)):
            s = intervals[i].start 
            e = intervals[i].end
            # check for conflict
            if s < current_end:
                return False
            # update values if no conflict
            current_start = s
            current_end = e 

        # return true if no issues
        return True 


# 0-30 15-20 5-10
# 0-30 5-10 15-20 
# s = 0 e = 30 
# is my new s > old e
# then move the s to new s 
# if violates is false, else loop finished we return true 