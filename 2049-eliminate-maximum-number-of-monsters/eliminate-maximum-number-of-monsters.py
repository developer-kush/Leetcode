class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        n = len(dist)
        time = sorted(dist[i]/speed[i] for i in range(n))
        time.append(float('-inf'))
        idx = 0
        while idx < time[idx]: idx += 1
        return idx