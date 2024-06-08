class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        if len(nums)<2: return False
        st=set([0])
        for i in range(1,len(nums)): 
            nums[i]+=nums[i-1]
        for i in range(1,len(nums)-1):
            if nums[i]%k in st: return True
            st.add(nums[i-1]%k)
        return nums[-1]%k in st