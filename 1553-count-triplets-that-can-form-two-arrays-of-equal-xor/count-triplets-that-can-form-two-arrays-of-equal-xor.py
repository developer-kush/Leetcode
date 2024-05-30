class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        for i in range(1, len(arr)): arr[i]^=arr[i-1]
        arr.insert(0, 0)
        d = defaultdict(list)
        for idx, val in enumerate(arr): d[val].append(idx)
        tot = 0
        for val in d.values():
            n = len(val)
            curr = 0
            for i in range(1, n):
                curr += i*(val[i]-val[i-1])
                tot += curr
            tot -= (n*(n-1))//2

        return tot