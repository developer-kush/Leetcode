class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums)
        for i in range(n+1):
            if (curr:=bin(i)[2:].rjust(n, '0')) not in nums:
                return curr