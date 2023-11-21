class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        freqs = {}
        for i in nums:
            curr = i-int(str(i)[::-1])
            freqs[curr] = freqs.get(curr,0) + 1
        return sum((freqs[k]*(freqs[k]-1))//2 for k in freqs)%(1000000007)