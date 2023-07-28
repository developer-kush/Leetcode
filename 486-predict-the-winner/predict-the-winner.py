class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:

        # @cache
        def rec(x,y,mode=0):
            if y<x: return 0
            
            if mode: return min(rec(x+1,y, 1-mode)-nums[x], rec(x,y-1, 1-mode)-nums[y])
            else:    return max(rec(x+1,y, 1-mode)+nums[x], rec(x,y-1, 1-mode)+nums[y])

        return rec(0, len(nums)-1)>=0