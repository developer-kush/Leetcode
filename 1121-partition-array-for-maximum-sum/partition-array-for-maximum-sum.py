class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:

        @cache
        def rec(idx):
            if idx >= len(arr): return 0
            res, currmax, cnt = 0, arr[idx], 0
            for i in range(idx, min(len(arr), idx+k)):
                currmax = max(currmax, arr[i])
                cnt += 1
                res = max(res, currmax*cnt + rec(i+1))
            return res

        return rec(0)