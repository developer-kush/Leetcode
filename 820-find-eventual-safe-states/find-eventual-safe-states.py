class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        res = set()

        visited = set()
        memo = {}
        
        def rec(root):
            if graph[root] == []: res.add(root); return True
            if root in memo: return memo[root]
            memo[root]=False

            safe = True
            for ne in graph[root]:  safe = safe and rec(ne)
            memo[root] = safe
            if safe: res.add(root)
            # print(root, " : ", safe)
            return safe

        for i in range(len(graph)):
            if i not in visited:
                rec(i)
        
        return sorted(res)