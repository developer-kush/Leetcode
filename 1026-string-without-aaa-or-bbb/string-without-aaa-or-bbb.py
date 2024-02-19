class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:
        if a > b:
            rems = a-b
            if rems*3 > a+b: return ("aab")*((a+b)//3) + "aab"[:(a+b)%3]
            return ('aab'*rems + 'ab'*(b-rems))
        rems = b-a
        if rems*3 > a+b: return ("bba")*((a+b)//3) + "bba"[:(a+b)%3]
        return ('bba'*rems + 'ba'*(a-rems))