class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        # m, n = len(nums), max(len(i) for i in nums)
        # res = []
        # for diag in range(m+n-1):
        #     if diag < m: x, y = diag, 0
        #     else: x, y = m-1, diag-m+1
        #     while x:
        #         if len(nums[x]) > y: res.append(nums[x][y])
        #         x, y = x-1, y+1
        #     if len(nums[0]) > diag: res.append(nums[0][diag])
        # return res
        idxvals = []
        for i, row in enumerate(nums):
            for j, val in enumerate(row): idxvals.append((i+j, -i, val))
        
        return [val[2] for val in sorted(idxvals)]
        