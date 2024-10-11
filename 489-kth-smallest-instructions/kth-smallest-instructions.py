class Solution:
    def kthSmallestPath(self, destination: List[int], k: int) -> str:

        @cache
        def factorial(n):
            if n <= 1: return 1
            return n*factorial(n-1)

        def nPr(n, copies):
            res = factorial(n)
            for num in copies: res //= factorial(num)
            return res

        v, h = destination

        res = ''
        for i in range(v+h):
            if h == 0: res += 'V'; continue
            if v == 0: res += 'H'; continue
            
            covered = nPr(v+h-1, [v, h-1]) # Covered if take V

            if covered < k: 
                res += 'V'
                v -= 1
                k -= covered
            else: 
                res += 'H'
                h -= 1
        
        return res