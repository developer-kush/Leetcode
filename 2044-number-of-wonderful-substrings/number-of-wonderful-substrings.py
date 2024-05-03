class Solution:
  def wonderfulSubstrings(self, word: str) -> int:
    tot = curr = 0
    cntMap = [0]*1024
    cntMap[0] = 1
    for ch in word:
        curr ^= (1 << (ord(ch)-97))
        tot += cntMap[curr] + sum(cntMap[curr^(1<<i)] for i in range(10))
        cntMap[curr] += 1
    return tot