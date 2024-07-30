class Solution:
    def minimumDeletions(self, s: str) -> int:
        n = len(s)

        sums = [int(val == 'a') for val in s]
        for i in range(1, n): sums[i] += sums[i-1]
        
        res = n - sums[-1]
        for i in range(n): res = max(res, sums[i] + (n-1-i - (sums[-1]-sums[i])))

        return n - res