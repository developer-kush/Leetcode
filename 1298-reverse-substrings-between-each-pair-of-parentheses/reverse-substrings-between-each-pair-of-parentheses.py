class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = [""]
        for i in s:
            if i == '(': stack.append("")
            elif i == ')': 
                temp = stack.pop()[::-1]
                stack[-1] += temp
            else: stack[-1] += i
        return stack[-1]