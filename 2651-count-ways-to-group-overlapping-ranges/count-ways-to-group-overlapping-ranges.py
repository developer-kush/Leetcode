class Solution:
    def countWays(self, ranges: List[List[int]]) -> int:
        ranges = sorted(ranges)
        _, end = ranges[0]
        tot = 1
        for s, e in ranges:
            if s <= end:
                end = max(end, e)
            else:
                tot+=1
                end = e
        return (1<<tot)%(10**9 + 7)