class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        rsum = sum(nums)
        lsum = 0
        for idx,i in enumerate(nums):
            rsum-=i
            if lsum == rsum: return idx
            lsum+=i
        return -1