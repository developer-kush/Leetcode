
class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        return int(ceil(log2(buckets)/log2((minutesToTest//minutesToDie)+1)))