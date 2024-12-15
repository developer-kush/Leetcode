class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        hp = [(-((p+1)/(t+1) - p/t), t, p) for p, t in classes]
        heapify(hp)

        for _ in range(extraStudents):
            _, t, p = heappop(hp)
            t, p = t+1, p+1
            heappush(hp, (-((p+1)/(t+1) - p/t), t, p))

        return sum(p/t for _, t, p in hp)/len(hp)