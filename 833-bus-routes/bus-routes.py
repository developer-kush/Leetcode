class Solution(object):
    def numBusesToDestination(self, routes, source, target):
        if source == target: return 0
        idxmap = defaultdict(list)

        for idx, route in enumerate(routes): 
            for node in route: idxmap[node].append(idx)

        travelled = set()
        visited = set([target])
        q = deque([[target,0]])
        while q: 
            curr, dist = q.popleft()
            for ne in idxmap[curr]:
                if ne in travelled: continue
                travelled.add(ne)
                for node in routes[ne]:
                    if node == source: return dist+1
                    if node in visited: continue
                    visited.add(node)
                    q.append([node, dist+1])
        return -1