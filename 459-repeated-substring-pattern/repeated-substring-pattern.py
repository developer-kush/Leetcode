class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        q1 = deque(s)
        q2 = deque(s)

        for _ in range(len(s)-1):
            q1.append(q1.popleft())
            if q1 == q2: return True
        
        return False