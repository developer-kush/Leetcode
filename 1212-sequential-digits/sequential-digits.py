class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        res = []
        for i in range(1, 10):
            for j in range(i+1, 10):
                num = int(''.join(map(str, range(i,j+1))))
                if num < low: continue
                if num > high: break
                res.append(num)
        return sorted(res)