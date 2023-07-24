class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        
        queue = [i for i in range(1, n+1)]
        popidx = 0

        for _ in range(n-1):
            popidx = (popidx+k-1)%len(queue)
            queue.pop(popidx)
            
            # queue.popleft()
        
        return queue[0]