class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        graph = {i:{} for i in range(n)}
        for idx, (u,v) in enumerate(edges):
            graph[u][v] = graph[v][u] = succProb[idx]

        probs = {i:0 for i in range(n)}
        probs[start] = 1
        q = deque([[start,1]])

        while q:
            curr, prob = q.popleft()
            
            for ne in graph[curr]:
                if probs[ne] < prob*graph[curr][ne]:
                    probs[ne] = graph[curr][ne]*prob
                    q.append([ne,probs[ne]])
        
        return probs[end]