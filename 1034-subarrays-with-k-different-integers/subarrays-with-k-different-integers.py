class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        tot = l = 0

        ctr = Counter()
        maxmap, maxhp = {}, []

        for r in range(len(nums)):
            maxmap[nums[r]] = r
            ctr[nums[r]] += 1
            heappush(maxhp, r)

            while len(maxmap) > k: 
                ctr[nums[l]]-=1
                if ctr[nums[l]] == 0: 
                    del maxmap[nums[l]]
                l += 1

            while (nums[maxhp[0]] not in maxmap) or maxmap[nums[maxhp[0]]] > maxhp[0] : heappop(maxhp)
            if len(maxmap) < k: continue

            tot += maxhp[0]-l+1

        return tot