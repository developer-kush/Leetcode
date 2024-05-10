class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        
        hp = [[arr[0]/arr[i], 0, i] for i in range(len(arr))]
        heapify(hp)

        for _ in range(k-1):
            _, a, b = heappop(hp)
            if a + 1 < b: heappush(hp, [arr[a+1]/arr[b], a+1, b])
        
        return [arr[hp[0][1]], arr[hp[0][2]]]