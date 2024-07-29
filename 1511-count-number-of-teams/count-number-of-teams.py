class Solution:
    def numTeams(self, rating: List[int]) -> int:
        n = len(rating)
        lmn, lmx, rmn, rmx = [0]*n, [0]*n, [0]*n, [0]*n

        for i in range(1, n):
            cnt = 0
            for j in range(i): cnt += (rating[i] > rating[j])
            lmn[i] = cnt
            lmx[i] = i-cnt
            
        for i in range(n-2, -1, -1):
            cnt = 0
            for j in range(n-1, i, -1): cnt += (rating[i] > rating[j])
            rmn[i] = cnt
            rmx[i] = n-1-i-cnt
        
        tot = 0
        for i in range(1, n-1):
            tot += lmn[i]*rmx[i] + lmx[i]*rmn[i] 

        return tot