class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        rng = tot = 0
        for num in nums:
            while n > rng and num > rng + 1: rng = ( rng << 1 ) | 1; tot += 1
            rng = rng + num
        while n > rng: rng = ( rng << 1 ) | 1; tot += 1
        return tot