class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        res = []
        pos = 0
        for i in range(1,n+1):
            if pos >= len(target): break
            res.append("Push")
            if target[pos] == i: 
                pos += 1
                continue
            res.append("Pop")
        return res