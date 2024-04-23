class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(set)
        for u, v in edges: 
            graph[u].add(v)
            graph[v].add(u)
        height = defaultdict(int)
        sub_heights = {}

        def dfs(node, par = -1):
            h = 0
            sub_h = {}
            for ne in graph[node]:
                if ne == par: continue
                curr = dfs(ne, node)
                sub_h[ne] = curr
                h = max(h, curr)
            height[node] = max(height[node], h)
            vals = sorted([(val, key) for key, val in sub_h.items()], reverse = True)[:2]
            sub_heights[node] = vals
            return h+1
        dfs(0)

        def fix(node, par = -1, val = 0):
            height[node] = max(height[node], val)
            if sub_heights[node] == []: return
            sub_h = sorted(sub_heights[node]+[(val, par)], reverse = True)
            for ne in graph[node]:
                if ne == par: continue
                if sub_h[0][1] == ne: fix(ne, node, sub_h[1][0]+1)
                else: fix(ne, node, sub_h[0][0]+1)
        fix(0)
        
        mn = min(height.values())
        return [key for key, val in height.items() if val == mn]