class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        tot = l = 0

        ctr = Counter()
        maxmap, maxhp = {}, []

        vis = set()

        for r in range(len(nums)):
            if nums[r] in maxmap: vis.add(maxmap[nums[r]])
            maxmap[nums[r]] = r
            ctr[nums[r]] += 1
            heappush(maxhp, r)

            while len(maxmap) > k: 
                ctr[nums[l]]-=1
                if ctr[nums[l]] == 0: 
                    vis.add(maxmap[nums[l]])
                    del maxmap[nums[l]]
                l += 1

            while maxhp[0] in vis: heappop(maxhp)
            if len(maxmap) < k: continue

            tot += maxhp[0]-l+1


        return tot