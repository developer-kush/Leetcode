class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        
        row = points[0]
        n = len(row)

        print(row)
        for i in range(1, len(points)):
            curr = points[i]

            leftscores = [val - n + idx + 1 for idx, val in enumerate(row)]
            lindices = [0]*n
            for i in range(1, n):
                if leftscores[i] > leftscores[lindices[i-1]]: lindices[i] = i
                else: lindices[i] = lindices[i-1]
                
            rightscores = [val - idx for idx, val in enumerate(row)]
            rindices = [n-1]*n
            for i in range(n-2, -1, -1):
                if rightscores[i] > rightscores[rindices[i+1]]: rindices[i] = i
                else: rindices[i] = rindices[i+1]

            # print(lindices, rindices)
            
            for i in range(n):
                l, r = lindices[i], rindices[i]
                lval = row[l]-(i-l)
                rval = row[r]-(r-i)
                # print(i, ":", lval, rval, "-", l, r)
                curr[i] += max(lval, rval)
            
            row = curr
            # print(row)

        
        return max(row)