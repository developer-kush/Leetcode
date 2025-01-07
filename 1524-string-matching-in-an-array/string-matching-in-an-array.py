class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        return [word for idx, word in enumerate(words) if any(word in x for i,x in enumerate(words) if i!=idx)]