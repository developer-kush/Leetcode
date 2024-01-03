class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        bank = [i.count('1') for i in bank if int(i)]
        return sum(bank[i]*bank[i+1] for i in range(len(bank)-1))