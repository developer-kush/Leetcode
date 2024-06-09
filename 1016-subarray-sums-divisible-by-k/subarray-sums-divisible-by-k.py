class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefixsum = [0]
        for i in nums: prefixsum.append(prefixsum[-1]+i)
        groups = {i:0 for i in range(k)}
        for i in prefixsum: groups[i%k]+=1
        
        tot = sum(groups[i]*(groups[i]-1)//2 for i in groups)
        return tot