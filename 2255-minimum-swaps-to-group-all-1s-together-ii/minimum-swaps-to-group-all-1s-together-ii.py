class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        zc = sum(1-num for num in nums)
        nums += nums[:zc]

        cc, res = 0, inf

        for i in range(zc): cc += 1-nums[i]
        res = min(res, zc-cc)

        for i in range(zc, len(nums)):
            cc += 1-nums[i]
            cc -= 1-nums[i-zc]
            res = min(res, zc-cc)
        
        return res