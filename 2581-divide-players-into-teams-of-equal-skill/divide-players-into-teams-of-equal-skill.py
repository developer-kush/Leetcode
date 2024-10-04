class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        tot=2*sum(skill)//len(skill)
        target=2*tot//len(skill)
        counts = Counter(skill)
        res=0
        for i in counts:
            while counts[i]>0:
                if counts[tot-i]==0:
                    return -1
                res+= i*(tot-i)
                counts[i]-=1
                counts[tot-i]-=1
        return res