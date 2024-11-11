class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        if all(nums[i]>nums[i-1] for i in range(1, len(nums))): return True
        if any(nums[i]<i+1 for i in range(len(nums))): return False

        sieve = [1]*1001
        sieve[0:2] = [0,0]
        for i in range(2,1000):
            for j in range(i*i,1001,i):
                sieve[j] = 0
        primes = [i for i in range(1000) if sieve[i]]
        nums.insert(0,0)

        for i in range(1,len(nums)):
            
            snum = nums[i] - nums[i-1]
            if snum <= 2 : continue
            pos = bisect_left(primes, snum) - 1
            nums[i] -= primes[pos]
        
        return all(nums[i]>nums[i-1] for i in range(1, len(nums)))