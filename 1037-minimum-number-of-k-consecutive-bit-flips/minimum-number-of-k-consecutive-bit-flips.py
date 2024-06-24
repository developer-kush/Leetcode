class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        q = deque()
        cnt = 0
        for idx in range(len(nums)-k+1):
            while q and idx - q[0] >= k: q.popleft()

            if len(q)&1: num = 1^nums[idx]
            else: num = nums[idx]
            
            if num == 0: cnt += 1; q.append(idx)
        
        for idx in range(len(nums)-k+1, len(nums)):
            while q and idx - q[0] >= k: q.popleft()

            if len(q)&1: num = 1^nums[idx]
            else: num = nums[idx]

            if num == 0: return -1

        return cnt