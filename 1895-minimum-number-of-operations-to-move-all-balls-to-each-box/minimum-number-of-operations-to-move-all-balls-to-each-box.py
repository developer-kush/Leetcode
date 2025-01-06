class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        res = []
        curr = balls = pref = suff = 0

        for i in range(len(boxes)-1, -1, -1):
            suff += balls
            balls += int(boxes[i])
        
        for i in range(len(boxes)):
            res.append(pref + suff)
            balls -= int(boxes[i])
            suff -= balls
            curr += int(boxes[i])
            pref += curr

        return res