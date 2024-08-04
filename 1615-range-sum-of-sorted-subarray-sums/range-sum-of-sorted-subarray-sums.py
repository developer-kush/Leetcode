class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        M = int(1e9 + 7)
        srt = []
        for i in range(n):
            sm = 0
            for j in range(i, n):
                sm += nums[j]
                srt.append(sm)
        srt.sort()
        return sum(srt[left-1: right])%M 