class Solution:
    def dailyTemperatures(self, t: List[int]) -> List[int]:
        stack = []
        res = []
        for i in range(len(t)-1,-1,-1):
            while len(stack) and t[stack[-1]] <= t[i]: 
                stack.pop()
            res.append(0 if not stack else stack[-1]-i)
            stack.append(i)
        return res[::-1]