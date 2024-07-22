class Solution:
    def minChanges(self, nums: List[int], k: int) -> int:
        n = len(nums)
        diffs = Counter()

        ctr = Counter()

        for i in range(n//2):
            a, b = nums[i], nums[-i-1]
            maxdiff = max(a, b, abs(a-k), abs(b-k))
            mindiff = abs(a-b)
            if a <= k or b <= k: mindiff = 0
            ctr[mindiff] += 1
            ctr[maxdiff+1] -= 1
            diffs[abs(a-b)] += 1
        
        cnt = 0
        res = float('inf')
        for i in range(k+1):
            cnt += ctr[i]
            movesreq = cnt + ((n//2)-cnt)*2
            res = min(res, movesreq - diffs[i])

        return res