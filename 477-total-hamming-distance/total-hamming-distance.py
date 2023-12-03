class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        ones, n = Counter(), len(nums)

        for num in nums:
            cnt = 0
            while num:
                if num&1: ones[cnt] += 1
                num >>= 1
                cnt += 1
        
        return sum(ones[i]*(n-ones[i]) for i in range(max(ones)+1))