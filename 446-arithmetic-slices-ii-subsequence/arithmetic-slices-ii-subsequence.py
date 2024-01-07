class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        st=set([nums[0]])
        memo=[dict() for _ in range(len(nums))]
        tot=0
        for j in range(1,len(nums)):
            for i in range(j):
                d = nums[j]-nums[i]
                tot+=memo[i][d] if d in memo[i] else 0
                memo[j][d] = memo[j].get(d,0)+(memo[i][d] if d in memo[i] else 0)+1
        return tot