class Trie:
    def __init__(self):
        self.counts = 0
        self.children = {}

    def add(self, word):
        for char in word:
            if char not in self.children: self.children[char] = Trie()
            self = self.children[char]
            self.counts += 1

    def getScore(self, word):
        total = 0
        for char in word:
            self = self.children[char]
            total += self.counts
        return total

class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        tr = Trie()
        for word in words: tr.add(word)
        return [tr.getScore(word) for word in words]