class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        
        idxvals = []
        for i, row in enumerate(nums):
            for j, val in enumerate(row): idxvals.append((i+j, -i, val))
        
        return [val[2] for val in sorted(idxvals)]