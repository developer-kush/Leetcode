class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        return [word for word, val in Counter((s1+" "+s2).split(' ')).items() if val==1]