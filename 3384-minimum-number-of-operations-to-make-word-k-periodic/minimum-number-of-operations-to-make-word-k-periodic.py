class Solution:
    def minimumOperationsToMakeKPeriodic(self, word: str, k: int) -> int:
        ctr = Counter()
        for i in range(len(word)//k):
            ctr[word[k*i: k*(i+1)]] += 1
        return len(word)//k - max(ctr. values())