class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals=sorted(intervals,key=lambda x:x[1])
        count=0

        le=float('-inf')
        for s,e in intervals:
            if s>=le:
                count+=1
                le=e
        
        return len(intervals)-count