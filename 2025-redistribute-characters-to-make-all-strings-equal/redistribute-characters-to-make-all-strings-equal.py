class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        n = len(words)
        ctr = Counter()
        for word in words:
            for char in word: ctr[char]+=1
        
        for val in ctr.values():
            if val%n: return False
            
        return True