class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        lo, hi = 0, len(people)-1
        tot = 0
        while lo<=hi:
            if lo!=hi and people[lo] + people[hi] <= limit: lo, hi = lo + 1, hi - 1
            else : hi -= 1
            tot += 1
        return tot