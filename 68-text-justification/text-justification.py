class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        currlen = 0
        curr = []

        def justify(words, spaces):
            if len(words) == 1: return words[0] + (' '*spaces)
            res = words[0]
            for i in range(1, len(words)):
                curradd = ceil(spaces/(len(words)-i))
                res += (' '*curradd) + words[i]
                spaces -= curradd
            return res

        for word in words:
            if currlen+len(word)+len(curr)>maxWidth:
                res.append(justify(curr, maxWidth-currlen))
                curr = [word]
                currlen = len(word)
            else: 
                currlen += len(word)
                curr.append(word)

        res.append(" ".join(curr).ljust(maxWidth))
        
        return res