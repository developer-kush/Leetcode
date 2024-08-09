class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        
        res = []

        
        next = {i:i+1 for i in range(n-1)}
        dist = n-1

        for u, v in queries:

            if u not in next: res.append(dist); continue

            start = next[u]

            while next[u] < v: 
                next[u] = next[next[u]]
                dist -= 1
            
            end = next[u]
            for i in range(start, end):
                if i in next: del next[i]
            
            res.append(dist)
        
        return res