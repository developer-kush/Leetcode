class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        totsum = sum(nums)
        lsum = 0
        for idx,i in enumerate(nums):
            if totsum-i-lsum == lsum: 
                return idx
            lsum+=i
        return -1