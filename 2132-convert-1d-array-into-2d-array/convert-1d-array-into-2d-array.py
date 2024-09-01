class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if m*n != len(original): return []
        return [original[n*i:n*(i+1)] for i in range(m)]