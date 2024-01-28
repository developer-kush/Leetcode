class Solution:
    def smallestValue(self, n: int) -> int:
        while True:
            curr = 0
            tempn = n

            for i in range(2, n):
                while n%i == 0:
                    n //= i
                    curr += i
                if n == 1: break
            
            if curr == 0 or curr == tempn: return tempn
            n = curr