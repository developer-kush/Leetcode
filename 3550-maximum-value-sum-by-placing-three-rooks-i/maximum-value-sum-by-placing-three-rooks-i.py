class Solution:
    def maximumValueSum(self, board: List[List[int]]) -> int:
        # for row in board: print(*row)

        n, m = len(board), len(board[0])

        positions = set()

        nums = []
        for i in range(n):
            for j in range(m):
                nums.append([board[i][j], i, j])

        nums.sort(reverse = True)

        def best_two(l, r, x, y):
            res = []
            for i in range(l, r):
                a, b, c = nums[i]
                if b!=x and y!=c: res.append([a, b, c])
                if len(res) == 50: return res
            return res
        
        mn = min(m, n)
        res = float('-inf')

        for i in range(1, 3*mn-1):

            num, x, y = nums[i]
            a = b = float('-inf')

            left = best_two(0, i, x, y)
            right = best_two(i+1, len(nums), x, y)

            for p1, p2, p3 in left:
                for q1, q2, q3 in right:
                    if p2 == x or q2 == x or p2 == q2: continue
                    if p3 == y or q3 == y or p3 == q3: continue
                    res = max(res, num + p1 + q1)

        return res