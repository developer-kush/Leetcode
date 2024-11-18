class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)

        code *= 2
        for i in range(1, len(code)): code[i] += code[i-1]
        def agg(l, r):
            if l == 0: return code[r]
            else: return code[r]-code[l-1]

        if k >= 0: return [agg(i+1, i+k) for i in range(n)]

        k = abs(k)

        return [agg(i-k, i-1) for i in range(n, 2*n)]