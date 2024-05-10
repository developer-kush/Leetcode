class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        fractions = [[arr[i], arr[j]] for i in range(len(arr)) for j in range(len(arr))]
        fractions = sorted(fractions, key = lambda x: x[0]/x[1])
        return fractions[k-1]