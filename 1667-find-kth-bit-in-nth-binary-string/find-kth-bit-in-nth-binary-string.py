class Solution:
    def findKthBit(self, n: int, k: int) -> str:

        def rec(n):
            if n == 1: return '0'

            res = rec(n-1)
            rev = "".join([ '0' if i=='1' else '1' for i in res])[::-1]
            # rev = str(~int(res, 2)).rjust(len(res),'0')[::-1]

            return res+"1"+rev

        s = rec(n)
        # print(s)

        return s[k-1]
