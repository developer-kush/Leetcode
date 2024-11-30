class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        for u, v in pairs: graph[u].append(v)

        out = {key:len(val) for key, val in graph.items()}
        inp = Counter()
        for k, v in graph.items():
            for x in v: inp[x] += 1
        
        start = [i for i in out if out[i]-inp[i]==1]
        start = start[0] if start else pairs[0][0]
        
        path = []
        st = [start]
        vis = set()

        while st:
            curr = st[-1]
            if graph[curr]:
                st.append(graph[curr].pop())
                continue
            else:
                while st and not graph[st[-1]]:
                    path.append(st[-1])
                    st.pop()
        
        return [[path[i+1], path[i]] for i in range(len(pairs)-1, -1, -1)]