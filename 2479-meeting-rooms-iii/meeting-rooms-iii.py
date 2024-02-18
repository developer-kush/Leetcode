from heapq import *

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        rooms=[0]*n
        meetings=sorted(meetings)
        fs,fe=meetings[0]
        free=list(range(1,n))
        heap=[[meetings[0][1],0]]
        rooms[0]=1
        for s,e in meetings[1:]:
            while len(heap) and nsmallest(1,heap)[0][0]<=s:
                me,r=heappop(heap)
                heappush(free,r)
            
            if not len(free):
                me,r=heappop(heap)
                e+=me-s
                heappush(free,r)
            
            newroom=heappop(free)
            heappush(heap,[e,newroom])
            rooms[newroom]+=1
        
        minindex=0
        for i in range(1,n):
            if rooms[i]>rooms[minindex]:
                minindex=i
        return minindex