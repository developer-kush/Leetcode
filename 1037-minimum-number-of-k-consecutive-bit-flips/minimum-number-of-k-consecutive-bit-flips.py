class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        q = deque()
        cnt = 0
        bp = len(nums)-k+1

        for idx in range(len(nums)):
            while q and idx - q[0] >= k: q.popleft()

            if len(q)&1: num = 1^nums[idx]
            else: num = nums[idx]

            if idx >= bp:
                if num == 0: return -1
            elif num == 0: cnt += 1; q.append(idx)
        
        return cnt