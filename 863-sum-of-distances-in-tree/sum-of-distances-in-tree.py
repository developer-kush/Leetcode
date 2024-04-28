class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1 : return [0]

        graph = {i:set() for i in range(n)}
        for u,v in edges:
            graph[u].add(v)
            graph[v].add(u)
        
        counts = {}
        def count(root,prev=-1):
            tot = 1
            for ne in graph[root]:
                if ne == prev: continue
                subcount = count(ne,root)
                tot+=subcount
                counts[(ne,root)] = subcount
                counts[(root,ne)] = n-subcount
            return tot
        count(0)

        def distsum(root,prev=-1):
            tot = 0
            for ne in graph[root]:
                if  ne == prev: continue
                tot += counts[(ne,root)] + distsum(ne,root)
            return tot
        
        res = [0]*n
        res[0] = distsum(0)

        def calcrem(root,prev):
            res[root] = res[prev] - counts[(root,prev)] + counts[(prev,root)]
            for ne in graph[root]:
                if ne == prev: continue
                calcrem(ne,root)
        for ne in graph[0]:
            calcrem(ne,0)

        return res
        


