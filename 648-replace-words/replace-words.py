class Trie:
    def __init__(self):
        self.is_end = False
        self.children = {}

    def add(self,val):
        for i in val:
            if i not in self.children:
                self.children[i] = Trie()
            self = self.children[i]
        self.is_end = True
    
    def findword(self,word):
        res = ""
        for i in word:
            if i not in self.children:
                return word
            res+=i
            self = self.children[i]
            if self.is_end:
                return res
        return word

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        tr = Trie()
        for word in dictionary:
            tr.add(word)
        
        s = sentence.split()
        return " ".join(list(map(tr.findword,s)))
