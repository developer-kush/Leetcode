class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        res = ["Push", "Pop"]*(target[0]-1)
        for idx in range(1, len(target)):
            res += ["Push"]
            res += ["Push", "Pop"]*(target[idx]-target[idx-1]-1)
        res.append("Push")
        return res