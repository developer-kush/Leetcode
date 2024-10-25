class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        res = [folder[0]]

        for f in folder[1:]:
            a, b = res[-1], f
            mn = min(len(a), len(b))
            if a[:mn] == b[:mn] and len(b) > mn and b[mn] == '/':
                continue
            res.append(b)

        return res