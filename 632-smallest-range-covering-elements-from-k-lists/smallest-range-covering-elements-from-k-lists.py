class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        numGrps = defaultdict(Counter)
        for idx, arr in enumerate(nums): 
            for val in arr: numGrps[val][idx] += 1

        srtKeys = sorted(numGrps)
        covcnt = Counter()

        l, mn = 0, float('inf')
        res = [] 

        for r in range(len(srtKeys)):
            for grp, val in numGrps[srtKeys[r]].items(): covcnt[grp] += val
            
            while l < r and all(covcnt[grp] > val for  grp, val in numGrps[srtKeys[l]].items()):
                for grp, val in numGrps[srtKeys[l]].items(): 
                    covcnt[grp] -= val
                l += 1
            
            if len(covcnt) == len(nums) and srtKeys[r]-srtKeys[l]+1 < mn:
                mn = srtKeys[r]-srtKeys[l]+1
                res = [srtKeys[l], srtKeys[r]]

        return res