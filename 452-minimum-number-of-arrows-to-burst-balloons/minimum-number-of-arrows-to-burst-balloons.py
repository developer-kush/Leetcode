class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points = sorted(points, key = lambda x: x[1])
        cnt = 1
        last = points[0][1]
        for i in range(1,len(points)):
            if points[i][0] > last:
                cnt += 1
                last = points[i][1]
        return cnt