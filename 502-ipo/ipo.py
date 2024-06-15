class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        n, ptr = len(profits), 0
        lst = sorted([[capital[i], profits[i]] for i in range(len(profits))])
        heap = []
        while ptr < n:
            if lst[ptr][0] > w: break
            item = [-lst[ptr][1], lst[ptr][0]]
            heappush(heap, item)
            ptr += 1

        for _ in range(k):
            if len(heap) == 0: break
            curr = heappop(heap)
            if curr[0] < 0: w -= curr[0]
            else: break
            while ptr < n :
                if lst[ptr][0] > w: break
                item = [-lst[ptr][1], lst[ptr][0]]
                heappush(heap, item)
                ptr += 1

        return w