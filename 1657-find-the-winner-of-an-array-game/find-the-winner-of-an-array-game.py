class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        if k >= len(arr): return max(arr)
        cnt, curr = 0, arr[0]
        for i in range(1, len(arr)):
            if arr[i] < curr: 
                cnt += 1
            else:
                cnt = 1
                curr = arr[i]
            if cnt == k: return curr
        return curr