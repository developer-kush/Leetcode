class Solution:
    def maxAmount(self, initialCurrency: str, pairs1: List[List[str]], rates1: List[float], pairs2: List[List[str]], rates2: List[float]) -> float:

        def solve(st, pairs, rates):
            mx_reach = st
            for _ in range(100):
                for idx, (u, v) in enumerate(pairs):
                    mx_reach[v] = max(mx_reach[v], mx_reach[u]*rates[idx])
                    mx_reach[u] = max(mx_reach[u], mx_reach[v]*(1/rates[idx]))

            return mx_reach

        res = solve(Counter({initialCurrency:1}), pairs1, rates1)
        res = solve(res, pairs2, rates2)

        return res[initialCurrency]