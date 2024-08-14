class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums = sorted(nums)

        def possible(x):
            res = 0
            tot, q = 0, deque()
            for num in nums:
                while q and num-q[0] > x: q.popleft()
                res += len(q)
                q.append(num)
            return res >= k
        
        l = 0
        r = nums[-1]-nums[0]

        while l < r:
            m = (l + r)>>1
            if possible(m): r = m
            else: l = m + 1
        
        return (l+r)>>1