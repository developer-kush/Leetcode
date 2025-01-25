class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        idxarr = [(val, idx) for idx, val in enumerate(nums)]
        idxarr.sort()
        
        groups = []
        curr = []
        
        for val, idx in idxarr:
            if (not curr) or (val-curr[-1][0] <= limit): curr.append((val, idx))
            else: 
                groups.append(list(curr))
                curr = [(val, idx)]
        if curr: groups.append(list(curr))
        
        
        gidxs = {}
        groupvals = []
        for idx, group in enumerate(groups):
            groupvals.append([val[0] for val in group][::-1])
            for cidx in [val[1] for val in group]:
                gidxs[cidx] = idx
        
        return [groupvals[gidxs[i]].pop() for i in range(len(nums))]