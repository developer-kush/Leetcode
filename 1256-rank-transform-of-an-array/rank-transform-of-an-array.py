class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        if not arr: return []
        
        order = sorted(range(len(arr)), key = lambda x: arr[x])
        res = [0]*len(arr)

        res[order[0]] = 1

        for i in range(1, len(order)):
            if arr[order[i-1]] == arr[order[i]]:
                res[order[i]] = res[order[i-1]]
            else:
                res[order[i]] = res[order[i-1]]+1
        
        return res