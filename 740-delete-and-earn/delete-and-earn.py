from collections import Counter

class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:

        freqs = Counter(nums)
        for key in freqs: freqs[key]*=key
        nums = sorted(freqs)

        if len(nums) == 1: return freqs[nums[0]]

        first = freqs[nums[0]]
        if nums[0]!=nums[1]-1: third = second = freqs[nums[0]] + freqs[nums[1]]
        else: third = second = max(freqs[nums[0]], freqs[nums[1]])

        for i in range(2, len(nums)):
            if nums[i-1]!=nums[i]-1: 
                third = freqs[nums[i]]+second
            else:  
                third = max(second, freqs[nums[i]]+first)

            first, second = second, third

        return third
        


# 10**18 -> O(1)
# 10**9 -> O(log n)
# 10**5 -> O(n)
# 10**4 -> O(n log n)
# 10**3 -> O(n^2)
# 10**2 -> O(n^3)
# 10 -> 2^n