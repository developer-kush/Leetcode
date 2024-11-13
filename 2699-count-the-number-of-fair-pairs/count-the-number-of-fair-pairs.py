class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        srt = []

        tot = 0
        for num in nums:
            lb, ub = lower - num, upper - num
            a, b = bisect_left(srt, lb), bisect_left(srt, ub+1)
            tot += b-a
            insort(srt, num)
        
        return tot