class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        md = sum(nums)%p
        if not md: return 0

        mp = {0:-1}
        res, curr = inf, 0

        for idx, num in enumerate(nums):
            curr = (curr+num)%p
            req = (curr+p-md)%p
            if req in mp: res = min(res, idx-mp[req])
            mp[curr] = idx
        
        return res if res != len(nums) else -1