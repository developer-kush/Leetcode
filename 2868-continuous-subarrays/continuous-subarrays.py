class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        res = l = 0
        mx, mn = [], []
        for i in range(len(nums)):

            heappush(mn, [nums[i], i])
            heappush(mx, [-nums[i], i])

            while abs(mn[0][0]+mx[0][0]) > 2: 
                l += 1
                while mn[0][1] < l: heappop(mn)
                while mx[0][1] < l: heappop(mx)
            
            res += (i-l+1)            

        return res