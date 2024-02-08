class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        indices = set()
        values = set()

        tot = 0

        for idx, val in enumerate(arr):
            if val in indices: indices.remove(val)
            else: values.add(val)
            if idx in values: values.remove(idx)
            else: indices.add(idx)

            if indices == values == set(): tot += 1
        
        return tot