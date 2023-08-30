class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        tot = 0
        last = nums[-1]
        
        for num in nums[-2::-1]:
            if num > last: 
                tot += ceil(num/last) - 1
                if num%last == 0: continue
                last = num//ceil(num/last)
            else: last = num
        
        return tot