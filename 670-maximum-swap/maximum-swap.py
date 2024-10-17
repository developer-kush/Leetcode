class Solution:
    def maximumSwap(self, num: int) -> int:
        res = num
        num = str(num)
        mono = list(num)
        for i in range(len(mono)-2, -1, -1): mono[i] = max(mono[i], mono[i+1])
        pos = 0
        while pos < len(num) and num[pos] == mono[pos]: pos+=1
        if pos == len(num): return res

        for i in range(pos+1, len(num)):
            if num[i] == mono[pos]:
                res = max(res, int(num[:pos]+num[i]+num[pos+1:i]+num[pos]+num[i+1:]))
        
        return res