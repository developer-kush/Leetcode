class Solution:
    def bestRotation(self, nums: List[int]) -> int:
        n = len(nums)
        rangeMap = Counter()

        # Marking rotatable ranges
        for idx in range(n):
            rangeMap[idx] += 1
            rangeMap[(idx-nums[idx])%n+1] -= 1

        # Finding the best rotational value
        tot = midx = mxval = 0
        for i in range(len(nums)):
            tot += rangeMap[i]
            if tot > mxval: midx, mxval = i, tot
        return midx