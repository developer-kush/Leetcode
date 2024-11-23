class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        n, m = len(box), len(box[0])

        for row in box:
            p = m-1
            for i in range(m-1, -1, -1):
                if row[i] == '*': p = i-1; continue
                if row[i] == '#':
                    row[i], row[p] = row[p], row[i]
                    p -= 1

        res = [[ box[n-j-1][i] for j in range(n)] for i in range(m)]
        return res