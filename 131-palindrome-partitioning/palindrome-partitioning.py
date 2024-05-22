class Solution:
    def partition(self, s: str) -> List[List[str]]:
        memo, n = {}, len(s)

        def isPalindrome(i,j):
            if (i,j) in memo: return memo[(i,j)]
            if s[i] != s[j]: ans = False
            elif j-i<=1: ans = True
            else : ans = isPalindrome(i+1,j-1)
            memo[(i,j)] = ans
            return ans
        
        res = []
        state = []

        graph = {i:[j for j in range(i,n) if isPalindrome(i,j)] for i in range(n)}

        def rec(pos):
            if pos == n: res.append(list(state)); return
            for ne in graph[pos]:
                state.append(s[pos:ne+1])
                rec(ne+1)
                state.pop()

        rec(0)

        return res



