class Solution:
    def nthUglyNumber(self, n: int) -> int:
        hp = [[1, 0, 0, 0]]
        at = { 1 }
        for i in range(n-1):
            num, f2, f3, f5 = heappop(hp)
            
            for a, b, c, d in [(num*2, f2+1, f3, f5), (num*3, f2, f3+1, f5), (num*5, f2, f3, f5+1)]:
                if a in at: continue
                heappush(hp, [a, b, c, d])
                at.add(a)
        
        return heappop(hp)[0]