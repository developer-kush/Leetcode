class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        ctr = Counter(nums)
        mx = max(ctr.values())
        
        return Counter(ctr.values())[mx]*mx