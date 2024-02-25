class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        num_sums = {}
        psum, res = 0, float('-inf')
        for num in nums:
            num_sums[num] = min(psum, num_sums.get(num, float('inf')))
            psum += num
            if num-k in num_sums:
                res = max(res, psum-num_sums[num-k])
            if num+k in num_sums:
                res = max(res, psum-num_sums[num+k])
        return 0 if res == float('-inf') else res