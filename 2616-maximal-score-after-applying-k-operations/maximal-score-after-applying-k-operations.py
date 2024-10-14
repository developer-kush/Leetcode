class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        nums = [-i for i in nums]
        tot = 0
        heapify(nums)
        for _ in range(k):
            curr = heappop(nums)
            tot -= curr
            heappush(nums, -(ceil((-curr)/3)))
            
        return tot