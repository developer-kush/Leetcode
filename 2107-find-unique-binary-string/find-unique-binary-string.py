class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        for i in range(len(nums)+1):
            if (curr:=bin(i)[2:].rjust(len(nums), '0')) not in nums:
                return curr