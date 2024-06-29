class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        res=[[] for _ in range(n)]
        graph={}
        for i in range(n):
            graph[i]=[]
        for u,v in edges:
            graph[u].append(v)
        
        for i in range(n):
            visited=set([i])
            stack=[i]
            while len(stack):
                curr=stack.pop()
                for ele in graph[curr]:
                    if ele not in visited:
                        res[ele].append(i)
                        visited.add(ele)
                        stack.append(ele)
        return res