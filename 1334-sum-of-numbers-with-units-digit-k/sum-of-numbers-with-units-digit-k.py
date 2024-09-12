class Solution:
    def minimumNumbers(self, num: int, k: int) -> int:
        if num == 0: return 0
        for i in range(1,11):
            if num%10 == (k*i)%10: 
                if num >= k*i: return i
                return -1
        return -1