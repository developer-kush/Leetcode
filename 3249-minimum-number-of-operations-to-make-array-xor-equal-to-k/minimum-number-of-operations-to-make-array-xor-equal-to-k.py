class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        xor = k
        for num in nums: xor ^= num
        tot = 0
        while xor:
            tot += xor&1
            xor >>= 1
        return tot