class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        nums.sort(reverse = True)
        ctr = Counter()
        for num in nums: ctr[num] = ctr[num*num]+1
        res = max(ctr.values())
        if res > 1: return res
        return -1