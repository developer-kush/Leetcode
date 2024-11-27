class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        second_teams = set(edge[1] for edge in edges)
        res = set(range(n)) - set(second_teams)
        if len(res) != 1: return -1
        return list(res)[0]