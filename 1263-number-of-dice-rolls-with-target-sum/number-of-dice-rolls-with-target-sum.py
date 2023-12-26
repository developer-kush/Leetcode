class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        
        def solve(n,target,memo={}):
            if (n,target) in memo: return memo[(n,target)]
            if n==1 and target<=k: return 1
            elif n<1: return 0
            elif target<=0: return 0
            
            tot=0
            for i in range(target-1,target-k-1,-1):
                if i<=0: break
                tot+=solve(n-1,i,memo) if (n-1,i) not in memo else memo[(n-1,i)]
            
            memo[(n,target)]=tot
            return tot
        
        return solve(n,target)%(10**9+7)