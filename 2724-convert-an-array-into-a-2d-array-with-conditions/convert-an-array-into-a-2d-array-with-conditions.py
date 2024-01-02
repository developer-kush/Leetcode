class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        ctr = Counter(nums)
        res = []
        cnt = len(nums)
        
        while cnt:
            curr = []
            for i in ctr:
                if ctr[i]:
                    curr.append(i)
                    ctr[i] -= 1
                    cnt -= 1
            res.append(list(curr))
        
        return res