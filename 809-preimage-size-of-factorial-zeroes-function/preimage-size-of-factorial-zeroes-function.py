arr = [305175781, 61035156, 12207031, 2441406, 488281, 97656, 19531, 3906, 781, 156, 31, 6]

class Solution:
    def preimageSizeFZF(self, k: int) -> int:
        k += 1

        for num in arr: k %= num
        if not k: return 0

        return 5