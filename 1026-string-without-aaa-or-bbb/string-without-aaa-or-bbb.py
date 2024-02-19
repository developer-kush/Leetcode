class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:
        if a > b:
            rems = a-b
            return ('aab'*rems + 'ab'*(b-rems))[:a+b]
        else:
            rems = b-a
            return ('bba'*rems + 'ab'*(a-rems))[:a+b]