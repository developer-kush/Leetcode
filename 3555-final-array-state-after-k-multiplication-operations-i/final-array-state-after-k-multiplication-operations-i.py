class Solution:
    def getFinalState(self, nums: List[int], k: int, m: int) -> List[int]:
        hp = [[val, idx] for idx, val in enumerate(nums)]
        heapify(hp)
        for _ in range(k):
            val, idx = heappop(hp)
            nums[idx]*=m
            heappush(hp, [val*m, idx])
        return nums