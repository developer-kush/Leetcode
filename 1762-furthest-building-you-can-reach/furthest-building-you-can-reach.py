class MaxHeap:
    def __init__(self,arr=[]):
        self.heap=[]
    
    def heapify(self):
        for i in range(len(self.heap)-1,-1,-1):
            self.heapifydown()
    
    def heapifyup(self,index):
        if index==0: return
        parent=(index-1)//2
        if self.heap[parent]<self.heap[index]:
            self.heap[parent],self.heap[index]=self.heap[index],self.heap[parent]
            self.heapifyup(parent)
            
    def heapifydown(self,index=0):
        left= (2*index) +1
        right=(2*index) +2
        while (left<len(self.heap) and self.heap[left]>self.heap[index])or (right<len(self.heap) and self.heap[right]>self.heap[index]):
            smaller=left if (right>=len(self.heap) or self.heap[left]>self.heap[right]) else right
            self.heap[index],self.heap[smaller]=self.heap[smaller],self.heap[index]
            index=smaller
            left=(2*index)+1
            right=(2*index)+2
        
    def push(self,val):
        self.heap.append(val)
        self.heapifyup(len(self.heap)-1)
    
    def pop(self):
        self.heap[0],self.heap[-1]=self.heap[-1],self.heap[0]
        temp=self.heap.pop()
        self.heapifydown()
        return temp
    
        
    
class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        heap=MaxHeap()
        n=len(heights)
        for i in range(1,n):
            if heights[i]<heights[i-1]: continue
            diff=heights[i]-heights[i-1]
            if diff<=bricks:
                heap.push(diff)
                bricks-=diff
            else:
                if ladders==0: return i-1
                elif len(heap.heap)==0:
                    ladders-=1
                    continue
                else:
                    heap.push(diff)
                    bricks-=diff
                    diff=heap.pop()
                    bricks+=diff
                    ladders-=1
                    if bricks<0: return i-1
        return n-1