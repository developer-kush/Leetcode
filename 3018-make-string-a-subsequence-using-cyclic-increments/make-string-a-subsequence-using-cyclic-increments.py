class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        strinc = lambda i:chr(((ord(i)-96) % 26) + 97)
        ptr = 0
        for i in str1:
            if str2[ptr] == i or str2[ptr] == strinc(i) : ptr+=1
            if ptr >= len(str2): return True
        return False