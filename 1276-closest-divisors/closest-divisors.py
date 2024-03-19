class Solution:
    def closestDivisors(self, num: int) -> List[int]:
        a, b = num + 1, num + 2
        for i in range(int(max(a, b)**0.5), 0, -1):
            if not a%i: return [i, a//i]
            if not b%i: return [i, b//i]