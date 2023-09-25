class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand)%groupSize: return False
        if groupSize == 1: return True

        hand = sorted(hand)
        curr = {}

        for val in hand:
            if val - 1 in curr:
                last = curr[val-1].pop()
                if not curr[val-1]: del curr[val-1]
                
                last += 1
                if last != groupSize:
                    if val not in curr: curr[val] = []
                    curr[val].append(last)
                
            else: 
                if val not in curr: curr[val] = []
                curr[val].append(1)
                
        return not curr