class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t=="":return ""
        freq={}
        for i in t:
            freq[i]=1+freq.get(i,0)
        curr={}
        have,need=0,len(freq)
        l,res,reslen=0,[-1,-1],inf
        for h in range(len(s)):
            curr[s[h]]=1+curr.get(s[h],0)
            if s[h] in freq and curr[s[h]]==freq[s[h]]:
                have+=1
            while have==need:
                if h-l+1<reslen:
                    res=[l,h]
                    reslen=h-l+1
                curr[s[l]]-=1
                if s[l] in freq and curr[s[l]]<freq[s[l]]:
                    have-=1
                l+=1
        
        return s[res[0]:res[1]+1] if reslen!=inf else ""