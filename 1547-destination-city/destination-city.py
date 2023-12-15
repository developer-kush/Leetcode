class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        mp = {}
        for u, v in paths: mp[u]=v
        curr = paths[0][0]
        while curr in mp: curr = mp[curr]
        return curr