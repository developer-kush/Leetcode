class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:

        dictWords = {word:idx for idx, word in enumerate(wordDict)}
        end = len(s)

        neighbors = defaultdict(list)
        for i in range(len(s)):
            curr = ""
            for j in range(i, len(s)):
                curr += s[j]
                if curr in dictWords: neighbors[i].append((j+1, dictWords[curr]))

        curr = []
        res = []
        def rec(node):
            nonlocal curr, res, end
            if node == end: res.append(" ".join(curr))
            elif node > end: return
    
            for ne, wordidx in neighbors[node]:
                curr.append(wordDict[wordidx])
                rec(ne)
                curr.pop()
        rec(0)

        return res