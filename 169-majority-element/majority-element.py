class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cnt = 0
        element = None

        for val in nums:
            if not cnt:
                cnt = 1
                element = val
            elif val == element: cnt += 1
            else: cnt -= 1
        
        return element