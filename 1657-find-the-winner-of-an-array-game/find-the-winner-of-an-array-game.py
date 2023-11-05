class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        if k >= len(arr): return max(arr)
        mx = max(arr)
        q = deque(arr)

        while q[0] != mx:
            cnt = 0
            a, b = q.popleft(), q.popleft()
            while cnt!=k and a > b:
                cnt += 1
                q.appendleft(a)
                q.append(b)
                a, b = q.popleft(), q.popleft()
    
            if cnt == k: return a

            if b > a: 
                q.appendleft(a)
                q.appendleft(b)
        
        return mx