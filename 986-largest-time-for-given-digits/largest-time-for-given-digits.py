class Solution:
    def largestTimeFromDigits(self, arr: List[int]) -> str:
        res = ""
        for i in range(4):
            for j in range(4):
                if i == j: continue
                for k in range(4):
                    if k in (i, j): continue
                    for l in range(4):
                        if l in (i, j, k): continue
                        a, b, c, d = arr[i], arr[j], arr[k], arr[l]
                        if int(10*a+b) <= 23 and int(10*c + d) < 60: 
                            res = max(res, f"{a}{b}:{c}{d}")
        return res