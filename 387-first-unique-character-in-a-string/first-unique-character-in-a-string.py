class Solution:
    def firstUniqChar(self, s: str) -> int:
        unique,duplicates=set(),set()
        for i in s:
            if i not in duplicates:
                if i in unique:
                    unique.remove(i)
                    duplicates.add(i)
                else:
                    unique.add(i)
        if len(unique)==0:
            return -1
        for i in range(len(s)):
            if s[i] in unique: return i
        