class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        def rec(i,d,currmax,memo={}):
            if (i,d,currmax) in memo: return memo[(i,d,currmax)]
            if i<d: return inf
            if i==0: return currmax
            c1= currmax + (rec(i-1,d-1,jobDifficulty[i-1],memo) if (i-1,d-1,jobDifficulty[i-1]) not in memo else memo[(i-1,d-1,jobDifficulty[i-1])])
            c2= rec(i-1,d,max(currmax,jobDifficulty[i-1]),memo) if (i-1,d,max(currmax,jobDifficulty[i-1])) not in memo else memo[(i-1,d,max(currmax,jobDifficulty[i-1]))]
            memo[(i,d,currmax)]=min(c1,c2)
            return memo[(i,d,currmax)]
        
        ans = rec(len(jobDifficulty),d,0)
        return ans if ans!=inf else -1