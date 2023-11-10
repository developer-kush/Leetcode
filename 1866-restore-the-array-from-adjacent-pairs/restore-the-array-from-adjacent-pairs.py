class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        adj = defaultdict(lambda : [])
        for u, v in adjacentPairs:
            adj[u].append(v)
            adj[v].append(u)
        
        res = []
        vis = set()
        for node in adj:
            if len(adj[node]) == 1:
                res.append(node)
                vis.add(node)
                for _ in range(len(adjacentPairs)):
                    node = adj[node][0] if adj[node][0] not in vis else adj[node][1]
                    vis.add(node)
                    res.append(node)
                break
        return res