class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        return [i for i, val in Counter(nums).items() if val == 1]