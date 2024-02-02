class Solution:
    def search(self, nums: List[int], t: int) -> int:
        
        lo,hi=0,len(nums)-1
        while lo!=hi:
            mid=lo+(hi-lo)//2
            if nums[mid]==t: return mid
            elif nums[lo]<=nums[mid] and t>=nums[lo] and t<=nums[mid]:
                hi=mid
            elif nums[lo]<=nums[mid]:
                lo=mid+1
            elif nums[mid+1]<=nums[hi] and t>=nums[mid+1] and t<=nums[hi]:
                lo=mid+1
            else:
                hi=mid
            
        
        if nums[lo]==t: return lo
        return -1
            
            