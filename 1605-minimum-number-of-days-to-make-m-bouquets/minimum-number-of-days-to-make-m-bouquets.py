class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if len(bloomDay) < m*k: return -1
        n = len(bloomDay)
        
        hp = []
        dp = [0]*n
        for i in range(n-1, -1, -1):
            heappush(hp, (-bloomDay[i], i))
            while hp[0][1] >= i + k: heappop(hp)
            dp[i] = -hp[0][0]
        
        def check(x, dp, n, k, m):
            ptr = cnt = 0
            while ptr < n:
                if ptr + k > n: break
                if dp[ptr] <= x: 
                    ptr = ptr + k
                    cnt += 1
                else: ptr += 1
                if cnt >= m: return True
            return cnt >= m
        
        uniques = sorted(set(bloomDay))
        l, r = 0, len(uniques)-1
        while l < r:
            mid = (l + r) >> 1
            possible = check(uniques[mid], dp, n, k, m)
            if possible: r = mid
            else: l = mid+1
        return uniques[l]