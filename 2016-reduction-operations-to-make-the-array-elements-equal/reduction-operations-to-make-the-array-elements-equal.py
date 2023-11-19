class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        ctr = Counter(nums)
        keys = sorted(ctr)

        return sum(idx*ctr[key] for idx, key in enumerate(keys))