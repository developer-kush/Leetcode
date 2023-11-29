class Solution:
    def hammingWeight(self, n: int) -> int:
        tot=0
        while n:
            n-=n&-n
            tot+=1
        return tot