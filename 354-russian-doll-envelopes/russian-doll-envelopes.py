class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort()
        arr = [[envelopes[0][1]]]
        for i in range(1, len(envelopes)):
            if envelopes[i-1][0]!=envelopes[i][0]: arr.append([])
            arr[-1].append(envelopes[i][1])
        
        for i in range(len(arr)): arr[i] = sorted(set(arr[i]), reverse = True)
        
        merged = []
        for group in arr:
            for num in group: merged.append(num)

        res = [merged[0]]
        for i in range(1, len(merged)):
            if merged[i] > res[-1]: res.append(merged[i])
            pos = bisect_left(res, merged[i])
            res[pos] = merged[i]

        return len(res)
