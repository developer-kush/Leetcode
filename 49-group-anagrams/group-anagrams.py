def getAnagram(word):
    anagram=[0 for _ in range(26)]
    for i in word: anagram[ord(i)-97]+=1
    return tuple(anagram)

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictionary={}
        for word in strs:
            anagram=str(sorted(word))
            if anagram not in dictionary: dictionary[anagram]=[]
            dictionary[anagram].append(word)
        res=[]
        for value in dictionary.values(): res.append(value)
        return res