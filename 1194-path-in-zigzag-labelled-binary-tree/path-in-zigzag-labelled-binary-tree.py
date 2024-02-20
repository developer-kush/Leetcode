class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        depth = ceil(math.log2(label+1))
        if not depth & 1: 
            label = (1 << (depth-1)) + (1 << depth)-1 - label

        res = []

        while label:
            res.append(label)
            label >>= 1
        
        res.reverse()

        for i in range(1, len(res), 2):
            lb, ub = 1 << i, (1 << (i+1))-1
            res[i] = ub + lb - res[i]

        return res