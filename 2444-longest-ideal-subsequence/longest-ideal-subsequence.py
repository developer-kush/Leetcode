class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        
        lngths = [0]*26
        for ch in s:
            i = ord(ch)-97
            lngths[i] = max(lngths[max(0, i-k): min(26, i+k+1)]) + 1
        return max(lngths)