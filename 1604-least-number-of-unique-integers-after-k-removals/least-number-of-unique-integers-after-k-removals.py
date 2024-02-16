class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        freqs = sorted(Counter(arr).values(), reverse=True)
        while freqs and k >= freqs[-1]: k -= freqs.pop()
        return len(freqs)