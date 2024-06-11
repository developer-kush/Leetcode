class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        indexes = {val:idx for idx, val in enumerate(arr2)}
        arr1.sort(key= lambda x: indexes[x] if x in indexes else len(arr2)+x)
        return arr1