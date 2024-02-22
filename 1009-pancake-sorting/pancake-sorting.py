class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        def revarr(pos):
            l, r = 0, pos
            while l < r: 
                arr[l], arr[r] = arr[r], arr[l]
                l, r = l+1, r-1
        
        res = []
        for i in range(len(arr)-1, 0, -1):
            if arr[i] != i+1: 
                idx = arr.index(i+1)
                revarr(idx)
                revarr(i)
                if idx: res.append(idx+1)
                res.append(i+1)
    
        return res


"""
3 2 4 1
4 2 3 1
1 3 2 4
3 1 2 4
2 1 3 4
1 2 3 4
"""