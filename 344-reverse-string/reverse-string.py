class Solution:
    def reverseString(self, s: List[str]) -> None:
        for _ in range(len(s)//2):
            s[_],s[-_-1]=s[-_-1],s[_]
    
        """
        Do not return anything, modify s in-place instead.
        """
        