class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        formable = []

        for word in dictionary:
            ptr = -1
            for char in word:
                ptr += 1
                while ptr < len(s) and s[ptr] != char: ptr += 1
            if ptr < len(s): formable.append(word)

        if not formable: return ""
        return min(formable, key = lambda x: [-len(x), x])