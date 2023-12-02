class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        ctr = Counter(chars)
        tot = 0
        for word in words:
            tot += len(word)
            for letter, val in Counter(word).items():
                if val > ctr[letter]: tot -= len(word); break
        return tot