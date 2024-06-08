class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        if len(nums)<2: return False
        st=set()
        for i in range(1,len(nums)): 
            nums[i]+=nums[i-1]
        if nums[-1]%k==0: return True
        for i in range(1,len(nums)-1):
            if nums[i]%k==0: return True
            if nums[i]%k in st:
                return True
            st.add(nums[i-1]%k)
        return nums[-1]%k in st