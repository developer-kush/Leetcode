class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res=[[1]]
        if numRows==1: return res
        res.append([1,1])
        if numRows==2: return res
        for _ in range(numRows-2):
            curr=[1]
            for i in range(1,len(res[-1])): curr.append(res[-1][i-1]+res[-1][i])
            curr.append(1)
            res.append(curr)
        return res