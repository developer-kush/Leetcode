class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        freqarr={}
        for i in words[0]:
            if i not in freqarr: freqarr[i]=0
            freqarr[i]+=1
        for i in range(1,len(words)):
            currfreq={}
            for c in words[i]:
                if c in freqarr:
                    if c not in currfreq: currfreq[c]=0
                    currfreq[c]+=1
            for ele in freqarr:
                if ele in currfreq: freqarr[ele]=min(freqarr[ele],currfreq[ele])
                else: freqarr[ele]=0
        res=[]
        for i in freqarr: res.extend([i]*freqarr[i])
        return res