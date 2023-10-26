arr = [
    6, 31, 156, 781, 3906, 19531, 97656, 488281, 
    2441406, 12207031, 61035156, 305175781, 1525878906
]

class Solution:
    def preimageSizeFZF(self, k: int) -> int:
        k += 1

        for num in reversed(arr): k %= num
        if not k: return 0

        return 5