
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        ctr = Counter(words)
        return sorted(ctr, key=lambda x: [-ctr[x],x])[:k]