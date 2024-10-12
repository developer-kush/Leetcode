class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:

        cnt = res = 0

        mp = Counter()
        for u, v in intervals: 
            mp[u] += 1
            mp[v+1] -= 1

        for key in sorted(mp):
            cnt += mp[key]
            res = max(res, cnt)
        
        return res