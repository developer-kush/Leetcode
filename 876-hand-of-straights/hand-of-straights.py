class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand)%groupSize: return False
        if groupSize == 1: return True

        hand = sorted(hand)
        curr = {}

        for val in hand:
            if val - 1 in curr and curr[val-1]:
                last = curr[val-1].pop() + 1
                if last != groupSize:
                    if val not in curr: curr[val] = []
                    curr[val].append(last)
            else: 
                if val not in curr: curr[val] = []
                curr[val].append(1)
                
        return not (curr and any(curr.values()))