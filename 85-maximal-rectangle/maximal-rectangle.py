class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        n, m = len(matrix), len(matrix[0])

        for j in range(m):
            matrix[0][j] = int(matrix[0][j])
            for i in range(1, n):
                matrix[i][j] = int(matrix[i][j])
                if matrix[i][j] == 0: continue
                matrix[i][j] += matrix[i-1][j]

        def histoRectangle(arr): 
            arr.append(0)
            n, ans = len(arr), 0
            stack = []
            for i in range(n):
                while stack and arr[stack[-1]] > arr[i]:
                    h = arr[stack.pop()]
                    if not stack: ans = max(ans, h*i)
                    else: ans = max(ans, (i-stack[-1]-1)*h)
                stack.append(i)
            return ans

        return max(histoRectangle(row) for row in matrix)