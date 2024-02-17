class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        ctr = Counter(answers)
        tot = 0

        for key, val in ctr.items():
            tot += (key+1)*ceil(val/(key+1))

        return tot