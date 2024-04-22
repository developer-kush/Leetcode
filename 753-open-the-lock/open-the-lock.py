class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if target == "0000": return 0
        
        deadends = set(deadends)
        if "0000" in deadends: return -1

        visited = set()
        q = deque([[0, "0000"]])
        
        while q:
            dist, curr = q.popleft()

            for i in range(4):

                k1 = curr[:i] + str((int(curr[i])+1)%10) + curr[i+1:]
                k2 = curr[:i] + str((int(curr[i])+9)%10) + curr[i+1:]
                if k1 == target or k2 == target: return dist+1

                if k1 not in visited and k1 not in deadends:
                    q.append([dist+1, k1])
                    visited.add(k1)
                
                if k2 not in visited and k2 not in deadends:
                    q.append([dist+1, k2])
                    visited.add(k2)
        
        return -1