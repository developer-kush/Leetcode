class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        diff = right-left
        res = ""
        cpt = 1
        while left or right:
            if (left&1 and right&1) and not cpt <= diff:  res += '1'
            else: res+='0'
            left, right = left>>1, right>>1
            cpt*=2
            
        if not res: return 0
        return int(res[::-1],2)