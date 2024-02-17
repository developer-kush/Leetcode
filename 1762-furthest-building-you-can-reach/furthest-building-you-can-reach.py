class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        heap = []
        n=len(heights)
        for i in range(1,n):
            if heights[i]<heights[i-1]: continue
            diff=heights[i]-heights[i-1]
            if diff<=bricks:
                heappush(heap, -diff)
                bricks-=diff
            else:
                if ladders==0: return i-1
                elif len(heap)==0:
                    ladders-=1
                    continue
                else:
                    heappush(heap, -diff)
                    bricks-=diff
                    diff= -heappop(heap)
                    bricks+=diff
                    ladders-=1
                    if bricks<0: return i-1
        return n-1