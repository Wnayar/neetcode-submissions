class Solution:
    # tc: O(n)
    # sc: O(1)
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        res = 0
        # sort by startign time ascending
        intervals.sort()
        prevEnd = intervals[0][1]

        if len(intervals) == 1:
            return res 

        for i in intervals[1:]:
            # check if current element start less then prevEnd which means overlapping
            if i[0] < prevEnd:
                # if overlapping greedily remove one which ends later 
                res += 1
                prevEnd = min(prevEnd, i[1])
            else:
                # not overlapping
                prevEnd = i[1]

        return res 