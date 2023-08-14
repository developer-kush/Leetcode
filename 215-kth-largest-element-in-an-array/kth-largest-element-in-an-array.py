class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int: 

        ptr = len(nums)-k
        
        def rec(l, r):
            
            if r == l: return nums[l]

            left, right = l, r
            pivot = nums[l]
            pos = l+1
            while pos <= r:
                if nums[pos] <= pivot:
                    nums[l], nums[pos] = nums[pos], nums[l]
                    l += 1
                    pos += 1
                else:
                    nums[r], nums[pos] = nums[pos], nums[r]
                    r-=1
            
            if l == ptr: return nums[l]
            elif l > ptr: return rec(left, l-1)
            else: return rec(l+1, right)


            # if l >= ptr: return rec(left, l)
            # return rec(l+1, right)
            return 0 

        
        res = rec(0, len(nums)-1)
        print("---")
        return res