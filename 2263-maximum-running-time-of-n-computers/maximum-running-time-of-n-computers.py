class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        if n == 1: return sum(batteries)
        if len(batteries) == n: return min(batteries)

        batteries = sorted(batteries, reverse=True)
        batteries, rempower = batteries[:n][::-1], sum(batteries[n:])

        for i in range(1,n):
            if rempower < i*(batteries[i]-batteries[i-1]):
                return batteries[i-1] + rempower//i
            rempower -= i*(batteries[i]-batteries[i-1])
        
        return batteries[-1] + rempower//n