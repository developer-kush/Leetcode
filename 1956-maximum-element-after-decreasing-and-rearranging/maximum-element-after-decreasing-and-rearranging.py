class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()

        last = 0
        for val in arr: last = min(val, last+1)
        
        return last