class Solution:
    def frequencySort(self, s: str) -> str:
        freqarr=Counter(s)
        
        return "".join(sorted([i*freqarr[i] for i in freqarr],key=lambda x:freqarr[x[0]],reverse=True))