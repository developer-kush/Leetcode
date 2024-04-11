class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        res = []
        for i in num:
            while res and k and res[-1] > i:
                res.pop()
                k-=1
            res.append(i)
        while res and k: 
            res.pop()
            k-=1
        res = "".join(res).lstrip('0')
        return res if res else '0'