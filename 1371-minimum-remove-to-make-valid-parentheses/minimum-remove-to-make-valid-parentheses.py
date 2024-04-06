class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        res = ""
        closes = s.count(')')
        opened = 0
        for i in s:
            if i == '(':
                if opened < closes:
                    res += '('
                    opened += 1
            elif i == ')':
                if opened:
                    res+= ')'
                    opened -= 1
                closes -= 1
            else:
                res += i
        return res