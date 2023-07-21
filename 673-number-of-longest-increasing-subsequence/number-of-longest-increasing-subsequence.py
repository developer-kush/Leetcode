class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1: return n

        lengths, cnts = [1]*n, [1]*n

        for i in range(1, n):
            for j in range(i):
                if nums[j] < nums[i]:
                    if lengths[j] >= lengths[i]:
                        lengths[i] = lengths[j] + 1
                        cnts[i] = cnts[j]
                    elif lengths[j]+1 == lengths[i]:
                        cnts[i] += cnts[j]

        max_len = max(lengths)
        res = 0
        for idx, i in enumerate(lengths):
            if i == max_len: res += cnts[idx]
        return res