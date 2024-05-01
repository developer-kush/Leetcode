class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch in word:
            idx = word.index(ch)
            return word[:idx+1][::-1] + word[idx+1:]
        else: return word