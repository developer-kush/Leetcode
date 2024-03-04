from collections import deque
class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        res = curr = 0
        l, r = 0, len(tokens)-1

        while l <= r:
            if tokens[l] <= power:
                power -= tokens[l]
                curr += 1
                l += 1
            elif curr:
                power += tokens[r]
                curr -= 1
                r -= 1
            else: break
            res = max(res, curr)
        
        return res