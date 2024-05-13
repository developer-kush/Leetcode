class Solution:
    def maximumGroups(self, grades: List[int]) -> int:
        for i in range(2, max(4, len(grades))):
            if ((i*(i+1)) >> 1 > len(grades)): return i-1
        return 0