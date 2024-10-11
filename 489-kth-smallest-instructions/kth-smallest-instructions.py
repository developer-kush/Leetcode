# global factorial

# size = 30
# factorial = [1]*size
# for i in range(2, size): factorial[i] = factorial[i-1]*i


class Solution:
    def kthSmallestPath(self, destination: List[int], k: int) -> str:
        global factorial

        # @cache
        # def factorial(n):
        #     if n <= 1: return 1
        #     return n*factorial(n-1)

        # def nCr(n, r):
        #     return factorial[n]//(factorial[n-r]*factorial[r])

        v, h = destination

        res = ''
        for i in range(v+h):
            if not h or not v: return res + "H"*h + "V"*v
            
            covered = comb(v+h-1, h-1) # Covered if take V

            if covered < k: 
                res += 'V'
                v -= 1
                k -= covered
            else: 
                res += 'H'
                h -= 1
        
        return res