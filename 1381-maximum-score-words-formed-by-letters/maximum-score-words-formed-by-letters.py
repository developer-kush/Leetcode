class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        fmap = Counter(letters)
        n = len(words)
        
        res = 0

        for selection in range(1<<n):
            currctr = Counter()
            ptr = 0
            while selection:
                if selection & 1: 
                    ctr = Counter(words[ptr])
                    for key in ctr:
                        currctr[key] += ctr[key]
                ptr += 1
                selection >>= 1

            if any(currctr[key] > fmap[key] for key in currctr): continue
            sc = sum(currctr[key]*score[ord(key)-97] for key in currctr)
            res = max(sc, res)

        return res