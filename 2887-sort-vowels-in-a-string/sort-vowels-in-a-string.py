class Solution:
    def sortVowels(self, s: str) -> str:
        
        s = [i for i in s]
        
        sortIndices = []
        for i in range(len(s)):
            if s[i].lower() in 'aeiou': sortIndices.append([i, s[i]])
        
        sortedForm = sorted(sortIndices, key=lambda x: x[1])
        
        for i in range(len(sortIndices)):
            s[sortIndices[i][0]] = sortedForm[i][1]
        
        return "".join(s)
            