from sortedcontainers import SortedDict

class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:

        cnt = res = 0

        mp = SortedDict()
        for u, v in intervals: 
            mp[u] = mp.get(u, 0) + 1
            mp[v+1] = mp.get(v+1, 0) - 1

        for key in mp:
            cnt += mp[key]
            res = max(res, cnt)
        
        return res