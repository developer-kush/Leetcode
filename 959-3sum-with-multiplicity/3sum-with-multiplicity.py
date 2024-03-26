class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        MOD = int(1e9 + 7)
        ctr = Counter(arr)
        arr = []
        for num in sorted(ctr): arr.extend([num]*min(ctr[num], 3))

        vis = set()

        def calc(a, b, c):
            if (a, b, c) in vis: return 0
            vis.add((a, b, c))
            if a == b == c: return ((ctr[a]*(ctr[a]-1)*(ctr[a]-2))//6)%MOD
            elif a == b: return ((ctr[a]*(ctr[a]-1)*ctr[c])>>1)%MOD
            elif a == c: return ((ctr[a]*(ctr[a]-1)*ctr[b])>>1)%MOD
            elif c == b: return ((ctr[b]*(ctr[b]-1)*ctr[a])>>1)%MOD
            else: return (ctr[a]*ctr[b]*ctr[c])%MOD
        
        res = 0
        for i in range(len(arr)-2):
            l, r = i+1, len(arr)-1
            while l < r:
                sm = arr[i]+arr[l]+arr[r]
                if sm > target: r -= 1
                elif sm < target: l += 1
                else:
                    res = (res + calc(arr[i], arr[l], arr[r]))%MOD
                    l += 1
                    r -= 1

        return res