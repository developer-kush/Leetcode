class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        n, idx = len(dist), 0
        time = sorted([dist[i]/speed[i] for i in range(n)])
        while idx < n and idx < time[idx]: idx += 1
        return idx