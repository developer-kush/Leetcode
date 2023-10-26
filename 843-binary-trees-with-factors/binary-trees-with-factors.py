class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        
        def rec(n,memo={}):
            if n in memo: return memo[n]
            elif n not in factordict: memo[n]=1
            else:
                tot=1
                for i,j in factordict[n]:
                    a= rec(i,memo) if i not in memo else memo[i]
                    b= rec(j,memo) if j not in memo else memo[j]
                    tot+=a*b
                memo[n]=tot
            return memo[n]
        
        
        valset=set(arr)
        arr=sorted(arr,reverse=True)
        
        factordict={}
        for i in range(len(arr)-1):
            for j in range(i+1,len(arr)):
                if not arr[i]%arr[j] and arr[i]//arr[j] in valset:
                    if arr[i] not in factordict: factordict[arr[i]]=[]
                    factordict[arr[i]].append([arr[j],arr[i]//arr[j]])
        memo={}
        tot = 0
        for i in arr:
            if i not in memo: rec(i,memo)
        return sum(memo.values())%(10**9+7)
        
        # return tot
    