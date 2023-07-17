class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        prev = list(nums)
        forward = list(nums)
        for i in range(1, len(nums)): 
            prev[i] = min(prev[i], prev[i-1])
        for i in range(len(nums)-2,-1,-1):
            forward[i] = max(forward[i], forward[i+1])
        
        for i in range(1,len(nums)-1):
            if prev[i-1] < nums[i] and forward[i+1] > nums[i]: return True
        return False



# Prefix sum property
# - Cover entire Prefix or array at a certain index
# - Should be able to calculate using value of previous index



# 0 1 2 5 4 7
# 0 0 0 0 0 0
# 7 7 7 7 7 7
