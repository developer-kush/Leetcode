class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        def count(n):
            res = 0
            while n:
                res += 1
                n = n & (n-1)
            return res

        c1, c2 = count(num1), count(num2)

        if c1 == c2: return num1
        if c1 > c2:
            for _ in range(c1-c2): num1 = num1 & (num1-1)
            return num1
        
        cnt = c2 - c1
        pos = 0
        while cnt:
            if not (num1>>pos)&1:
                cnt -= 1
                num1 = num1 | (1<<pos)
            pos += 1
        
        return num1