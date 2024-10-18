class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        mxor = reduce(lambda a, b: a | b, nums)
        n = len(nums)

        @lru_cache
        def rec(pos, sc):
            nonlocal n, nums, mxor
            if pos >= n: return int(sc==mxor)
            take = rec(pos+1, sc|nums[pos])
            notake = rec(pos+1, sc)
            return take + notake

        return rec(0, 0)