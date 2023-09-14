class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = {}
        for fr, to in tickets:
            if fr not in graph: graph[fr] = []
            graph[fr].append(to)
        for key in graph: graph[key] = sorted(graph[key])
        
        visited = set()
        res = []

        def rec(root):
            res.append(root)
            if len(visited) == len(tickets): return True
            if root in graph:
                for idx, city in enumerate(graph[root]):
                    pair = (root, idx)
                    if pair in visited: continue
                    visited.add(pair)
                    if rec(city): return True
                    visited.remove(pair)
            res.pop()

            return False
        
        rec("JFK")
        return res
