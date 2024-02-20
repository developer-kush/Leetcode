class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []

        for ch in s:
            if not stack: stack.append([ch, 1])
            elif ch == stack[-1][0]: stack[-1][1] += 1
            else: stack.append([ch, 1])
            
            if stack[-1][1] == k: stack.pop()
        
        res = ""
        for ch, cnt in stack: res += ch*cnt
        return res