class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr = sorted(arr)

        last = 1
        for i in range(1, len(arr)): last = min(arr[i], last+1)
        
        return last