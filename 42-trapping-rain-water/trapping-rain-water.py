class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)
        if n<=2: return 0
        right=list(height)
        currmax=0
        for i in range(n-2,-1,-1): right[i]=max(right[i],right[i+1])
        tot=0
        for i in range(n):
            if height[i]>=currmax:
                currmax=height[i]
                continue
            curr = min(currmax,right[i])-height[i]
            if curr>0: tot+=curr
        return tot