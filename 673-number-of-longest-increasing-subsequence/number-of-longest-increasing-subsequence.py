class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1: return n

        lengths = [1] * n
        counts = [1] * n

        for i in range(1, n):
            for j in range(i):
                if nums[j] < nums[i]:
                    if lengths[j] >= lengths[i]:
                        lengths[i] = lengths[j] + 1
                        counts[i] = counts[j]
                    elif lengths[j] == lengths[i]-1:
                        counts[i] += counts[j]

        max_len = max(lengths)
        res = 0
        for idx, i in enumerate(lengths):
            if i == max_len: res += counts[idx]
        return res