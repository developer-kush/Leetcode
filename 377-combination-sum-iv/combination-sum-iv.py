class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)

        @cache
        def rec(target):
            if target == 0: return 1
            if target < 0: return 0

            ways = 0
            for i in nums:
                if i<=target: ways += rec(target-i)
                else: break

            return ways
        
        return rec(target)