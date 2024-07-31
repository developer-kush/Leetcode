class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        n = len(books)
        dp = [inf]*n
        dp[0] = books[0][1]

        for i in range(1, n):
            width = books[i][0]
            mxhgt = books[i][1]
            dp[i] = mxhgt + dp[i-1]
            for j in range(i-1, -1, -1):
                width += books[j][0]
                mxhgt = max(mxhgt, books[j][1])
                if width > shelfWidth: break
                if j: dp[i] = min(dp[i], mxhgt + dp[j-1])
                else: dp[i] = min(dp[i], mxhgt)
    
        return dp[-1] if dp[-1] != inf else 0