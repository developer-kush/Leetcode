class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        ctr = Counter(nums)
        vals = [ctr[key] for key in sorted(ctr)]
        return sum(idx*vals[idx] for idx in range(len(vals)))