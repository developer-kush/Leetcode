from typing import List


class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        sm=sum(nums)
        if sm<x: return -1
        elif sm==x: return len(nums)

        prefixsum=list(nums)
        suffixsum=list(nums)
        for i in range(1,len(nums)): prefixsum[i]+=prefixsum[i-1]
        for i in range(len(nums)-2,-1,-1): suffixsum[i]+=suffixsum[i+1]
        prefixsum.insert(0,0)
        suffixsum.append(0)
        prefixsumindexdict={}
        for i in range(len(prefixsum)):
            if prefixsum[i] not in prefixsumindexdict: prefixsumindexdict[prefixsum[i]]=i
        currmin=float('inf')
        for i in range(1,len(suffixsum)+1):
            if x-suffixsum[-i] in prefixsumindexdict:
                currmin=min(currmin,i+prefixsumindexdict[x-suffixsum[-i]]-1)
        if currmin==float('inf'): return -1
        return currmin   
