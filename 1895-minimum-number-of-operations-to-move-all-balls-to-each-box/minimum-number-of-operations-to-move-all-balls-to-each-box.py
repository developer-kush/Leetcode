class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        res = [0]*len(boxes)
        curr = balls = pref = suff = 0

        for i in range(len(boxes)-1, -1, -1):
            suff += balls
            balls += int(boxes[i])
        
        for i in range(len(boxes)):
            res[i] = pref + suff
            balls -= int(boxes[i])
            suff -= balls
            curr += int(boxes[i])
            pref += curr

        return res