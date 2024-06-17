
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        for i in range(int(sqrt(c))+1):
            if ((c-i*i)**0.5)%1==0:
                return True
        return False