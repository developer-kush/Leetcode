class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        fill = mean*(n+len(rolls)) - sum(rolls)
        
        if fill < n or fill > 6*n: return []

        res = []
        ls = 0
        for i in range(n):
            rs = n-1-i
            res.append(min(6, fill-ls-rs))
            ls += res[-1]

        return res