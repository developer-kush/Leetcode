class Solution:
    def fib(self, n: int) -> int:
        if n <= 1: return n
        
        first, second = 0, 1

        for i in range(2,n+1):
            third = first + second
            first = second
            second = third

        return third
