class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        mxln = max(len(str(num)) for num in nums)
        nums = sorted(nums, reverse = True, key=lambda x: str(x)*mxln)
        res = ''.join(map(str, nums)).lstrip('0').rjust(1, '0')
        return res