class Solution:
    def maximumInvitations(self, favorite: List[int]) -> int:
        n = len(favorite)

        # fences
        re = defaultdict(list)
        safe = set()

        vis = [-2]*n

        def maxfind(x):
            res = 0
            vis[x] = -1
            for ne in re[x]:
                if ne in safe: continue
                res = max(res, maxfind(ne))
            return res+1
        
        for i in range(n):
            re[favorite[i]].append(i)
            if favorite[favorite[i]] == i: 
                safe.add(i)
                vis[i] = -1
        
        ansa = len(safe)

        for root in safe:
            ansa += maxfind(root) - 1
        
        # largest cycle
        ansb = 0

        for i in range(n):
            if vis[i] == -2:
                cnt = 0
                thisrun = set()
                while vis[i] == -2:
                    thisrun.add(i)
                    vis[i] = cnt
                    cnt += 1
                    i = favorite[i]
                if i not in thisrun: continue
                ansb = max(ansb, cnt - vis[i])

        return max(ansa, ansb)