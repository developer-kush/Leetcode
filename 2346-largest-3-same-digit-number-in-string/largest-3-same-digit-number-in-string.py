class Solution:
    def largestGoodInteger(self, num: str) -> str:
        res = found = 0
        for i in range(1, len(num)-1):
            if num[i-1]==num[i]==num[i+1]: res, found = max(res, int(num[i])), True
        if found: return str(res)*3
        return ""