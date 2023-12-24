class Solution:
    def minOperations(self, s: str) -> int:
        rev = { '0':'1', '1':'0'}

        change, nochange = list(s), list(s)
        change[0] = rev[change[0]]

        def getsc(arr):
            tot = 0
            for i in range(1, len(arr)):
                if arr[i-1]==arr[i]:
                    arr[i]=rev[arr[i]]
                    tot += 1
            return tot
        
        return min(getsc(change)+1, getsc(nochange))