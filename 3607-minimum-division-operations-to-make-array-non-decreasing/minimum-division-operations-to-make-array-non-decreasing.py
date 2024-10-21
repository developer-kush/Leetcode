class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        tot = 0

        for i in range(n-2, -1, -1):
            if nums[i] <= nums[i+1]: continue
            tot += 1
            for x in range(2, int(nums[i]**0.5)+1):
                if nums[i]%x == 0:
                    nums[i] = x
                    break
            else: return -1
            if nums[i] > nums[i+1]: return -1
        
        return tot