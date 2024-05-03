class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        st = set()
        res = -1
        for val in nums:
            if -val in st: res = max(res, abs(val))
            st.add(val)
        return res