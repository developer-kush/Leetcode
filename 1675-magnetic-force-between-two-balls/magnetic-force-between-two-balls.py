class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        
        def check(x):
            cnt = 1
            taken = position[0]
            for val in position:
                if val >= taken + x: 
                    cnt += 1
                    taken = val
                if cnt == m: return True
            return cnt >= m
        
        l, r = 0, max(position)
        while l < r: 
            mid = (l+r+1)>>1
            if check(mid): l = mid
            else: r = mid - 1
        return l