class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        ctr = Counter(arr)
        return max(ctr, key=lambda x: ctr[x])