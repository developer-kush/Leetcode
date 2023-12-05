class Solution:
    def numberOfMatches(self, n: int) -> int:
        cnt=0
        while n>1:
            cnt += n>>1
            n = (n+1)>>1
        return cnt