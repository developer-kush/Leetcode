class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        valdict={}
        dups=0
        for i in range(k):
            if nums[i] not in valdict:
                valdict[nums[i]]=1
            else:
                valdict[nums[i]]+=1
                if valdict[nums[i]]==2:
                    dups+=1
        currsum=sum(nums[:k])
        tot=currsum if dups==0 else 0
        for i in range(k,len(nums)):
            valdict[nums[i-k]]-=1
            if valdict[nums[i-k]]==1:
                dups-=1
            if nums[i] not in valdict:
                valdict[nums[i]]=0
            valdict[nums[i]]+=1
            if valdict[nums[i]]==2:
                dups+=1
            currsum+=nums[i]-nums[i-k]
            if dups==0:
                tot=max(tot,currsum)
        
        return tot