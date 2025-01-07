class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        return [
            word for word in words
            if any(word in x for x in words if x!=word)
        ]