class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        bsarr = [[0, -1]]
        for i in range(1, n): nums[i] += nums[i-1]

        print(nums)

        res = inf
        
        for r in range(n):
            while bsarr and bsarr[-1][0] >= nums[r]: bsarr.pop()
            bsarr.append([nums[r], r])
            tgt = nums[r]-k

            if tgt < bsarr[0][0] : continue
            
            pos = bisect_left(bsarr, [tgt+1, -1])-1
            # print(f"{bsarr = }")
            # print(f"tgt: {tgt} pos: {pos} | r: {r} tgtval: {bsarr[pos][1]} curr: {r-bsarr[pos][1]}")
            res = min(res, r-bsarr[pos][1])

        return -1 if res is inf else res