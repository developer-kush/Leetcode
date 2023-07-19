class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key = lambda x: x[1])

        print(intervals)
        lastIDX = intervals[0][1]
        cnt = 0
        for s, e in intervals[1:]:
            if s<lastIDX: cnt += 1
            else: lastIDX = e

        return cnt

# 1-6
# 2-6
# 3-6
