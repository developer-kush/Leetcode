class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        travel.append(0)
        res=0
        currdist=0
        gfarthest=mfarthest=pfarthest=0
        g=m=p=0
        for i in range(len(garbage)):
            garbage[i]=collections.Counter(garbage[i])
            if 'G' in garbage[i]: g,gfarthest=g+garbage[i]['G'],currdist
            if 'M' in garbage[i]: m,mfarthest=m+garbage[i]['M'],currdist
            if 'P' in garbage[i]: p,pfarthest=p+garbage[i]['P'],currdist
                
            currdist+=travel[i]
        
        res=pfarthest+gfarthest+mfarthest+p+m+g
        return res
        