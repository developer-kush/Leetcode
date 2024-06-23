class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        
        mn, mx, l, res = [], [], 0, 0

        for r in range(len(nums)):
            heappush(mn, (nums[r], r))
            heappush(mx, (-nums[r], r))
            while abs(mn[0][0]+mx[0][0]) > limit:
                min_ele = min(mn[0][1], mx[0][1])
                l = min_ele + 1
                while mn[0][1] < l: heappop(mn)
                while mx[0][1] < l: heappop(mx)
            res = max(res, r-l+1)
        
        return res