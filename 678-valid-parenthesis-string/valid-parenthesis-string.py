class Solution:
    def checkValidString(self, s: str) -> bool:
        
        opens = closes = 0

        for ch in s:
            if ch != ')': opens += 1
            else: opens -= 1
            if opens < 0: return False
        
        for ch in s[::-1]:
            if ch !='(': closes += 1
            else: closes -= 1
            if closes < 0: return False
        
        return True