class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        totxor = 0
        for val in derived: totxor ^= val

        return totxor == 0