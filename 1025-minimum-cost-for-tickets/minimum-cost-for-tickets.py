class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:

        memo = {}

        def rec(pos, covered):
            if pos >= len(days): return 0
            if days[pos] <= covered: return rec(pos+1, covered)
            if pos in memo : return memo[pos]
            res = min(costs[0]+rec(pos+1,days[pos]), costs[1]+rec(pos+1,days[pos]+6), costs[2]+rec(pos+1,days[pos]+29))
            memo[pos] = res
            return memo[pos]
            
        return rec(0, 0)