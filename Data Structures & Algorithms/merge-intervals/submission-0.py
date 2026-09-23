class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda i: i[0])
        res = [intervals[0]]

        for start, end in intervals:
            # merge 
            if start <= res[-1][1]:
                res[-1][1] = max(res[-1][1], end)
            # dont need to merge
            else:
                res.append([start, end])
        
        return res