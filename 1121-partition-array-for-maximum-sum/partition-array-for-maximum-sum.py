class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:

        dp = [0]*(len(arr)+1)

        for idx in range(len(arr)-1, -1, -1):
            res, currmax, cnt = 0, arr[idx], 0
            for i in range(idx, min(len(arr), idx+k)):
                currmax = max(currmax, arr[i])
                cnt += 1
                res = max(res, currmax*cnt + dp[i+1])
            dp[idx] = res

        return dp[0]