class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digitmap = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}

        if not digits: return []

        res = list(digitmap[digits[0]])

        for digit in digits[1:]:
            new_curr = []
            for char in digitmap[digit]:
                for prev in res: new_curr.append(prev+char)
            res = new_curr

        return sorted(res, reverse=True)