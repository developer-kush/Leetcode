class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:

        def kadaneModified(arr, res=0, curr=0, currmin=0):
            for num in arr:
                curr+=num
                currmin = min(currmin, curr)
                res = max(res, curr-currmin)
            return (res, curr, currmin)

        if k == 1: return kadaneModified(arr)[0]

        tot = sum(arr) * (k-2)
        res, curr, currmin = kadaneModified(arr)
        possible = kadaneModified(arr, res, curr, currmin)[0]
        curr += tot
        currmin = min(currmin, curr)
        res = max(res, curr-currmin)

        res, curr, currmin = kadaneModified(arr, res, curr, currmin)

        return max(possible, res) % int(1e9 + 7)