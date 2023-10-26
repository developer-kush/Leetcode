class Solution:
    def bestRotation(self, nums: List[int]) -> int:
        n = len(nums)
        rangeMap = Counter()

        # Marking rotatable ranges
        for idx, num in enumerate(nums):
            l, r = idx, (idx-num+n)%n
            # print(num, ":", f"{l} , {r}".rjust(7,' '), ":", end=" ")
            rangeMap[l] += 1
            rangeMap[r+1] -= 1

        # print("vals :",*[rangeMap[i] for i in range(n)])

        # Finding the best rotational value
        tot = midx = mxval = 0
        for i in range(len(nums)):
            tot += rangeMap[i]
            # print(tot, end=" ")
            if tot > mxval: midx, mxval = i, tot
        return midx
'''
---
--- -
   --
-----
 -
'''