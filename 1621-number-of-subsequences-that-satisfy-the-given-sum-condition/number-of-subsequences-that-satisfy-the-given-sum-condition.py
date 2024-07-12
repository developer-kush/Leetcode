class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:

        M = int(1e9+7)

        nums = sorted(nums)
        tot = 0

        for idx, i in enumerate(nums):
            if i > (target>>1): break
            if target-i > nums[-1]: dist = len(nums) - idx - 1
            else:
                pos = bisect_right(nums, target - i)
                if pos >= len(nums): dist = len(nums) - idx - 1
                elif nums[pos] > (target - i): dist = pos - 1 - idx 
                else: dist = pos - idx 
            if dist < 0: break
            tot = (tot + (1<<dist))%M

        return tot % M