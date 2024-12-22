class Solution:
    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        queries = [[u, v, i] for i, (u, v) in enumerate(queries)]
        for i in range(len(queries)):
            if queries[i][0] > queries[i][1]: 
                queries[i][0], queries[i][1] = queries[i][1], queries[i][0] 
        queries.sort(key = lambda x: x[1])
        queries = queries[::-1]

        res = [-1]*len(queries)
        hp = []

        for i in range(len(heights)):
            while queries and queries[-1][1] <= i: 
                u, v, x = queries.pop()
                lookout = max(heights[u], heights[v])
                if heights[u] == heights[v] and u != v: lookout += 1
                elif heights[u] > heights[v]: lookout += 1
                heappush(hp, (lookout, x))

            while hp and hp[0][0] <= heights[i]:
                res[hp[0][1]] = i
                heappop(hp)

        return res