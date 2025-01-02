class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        memo = [0]*len(words)
        if words[0][0] in 'aeiou' and words[0][-1] in 'aieou': memo[0] = 1
        for i in range(1,len(words)):
            memo[i] = memo[i-1]
            if words[i][0] in 'aeiou' and words[i][-1] in 'aeiou': memo[i] += 1
        res = []
        for l,r in queries:
            if l == 0: res.append(memo[r])
            else: res.append(memo[r]-memo[l-1])
        return res