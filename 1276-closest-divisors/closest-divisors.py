class Solution:
    def closestDivisors(self, num: int) -> List[int]:
        def findClosest(n):
            for i in range(int(n**0.5), 0, -1):
                if not n%i: return [i, n//i]
        
        a, b = findClosest(num+1), findClosest(num+2)
        return min(a, b, key=lambda x: abs(x[0]-x[1]))