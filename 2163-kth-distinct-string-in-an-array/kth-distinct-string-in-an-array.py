class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        ctr = Counter(arr)
        for val in arr:
            if ctr[val] > 1: continue
            k -= 1
            if k == 0: return val
        return ""