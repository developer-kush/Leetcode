class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:

        # Helper makeGroups function

        def makeGroups(meets):
            g = defaultdict(list)
            for s, e in meets:
                g[s].append(e)
                g[e].append(s)
            
            res = []
            visited = set()
            for start in g:
                if start in visited: continue
                s = [start]
                group = []
                while s:
                    curr = s.pop()
                    group.append(curr)
                    for ne in g[curr]:
                        if ne in visited: continue
                        visited.add(ne)
                        s.append(ne)

                res.append(group)
            
            return res
        
        # grouping meetings
        meetings.sort(key= lambda x: x[2])
        meetGroups = [[(meetings[0][0], meetings[0][1])]]

        for i in range(1, len(meetings)):
            if meetings[i][-1] != meetings[i-1][-1]: meetGroups.append([])
            meetGroups[-1].append(tuple(meetings[i][:2]))

        res = set({0, firstPerson})

        for meets in meetGroups:
            groups = makeGroups(meets)
            for group in groups:
                for val in group:
                    if val in res:
                        for val in group: res.add(val)
                        break
        
        return sorted(res)