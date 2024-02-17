class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        return sum(key*ceil(val/key) for key, val in Counter(val+1 for val in answers).items())