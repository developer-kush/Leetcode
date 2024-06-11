class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        taken = [0]
        tot = csum = 0

        for val in nums:
            csum += val
            r, l = csum - lower, csum - upper
            if r < taken[0] or l > taken[-1]: insort(taken, csum); continue
            p1 = bisect_left(taken, l)
            p2 = bisect_left(taken, r+1)
            tot += p2-p1
            insort(taken, csum)

        return tot