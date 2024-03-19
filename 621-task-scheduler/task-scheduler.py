class Solution:
    def leastInterval(self, tasks, n):
        ctr = Counter(tasks)
        uniques = sorted(set(tasks), key=lambda x: -ctr[x])
        res = len(tasks)
        for idx, val in enumerate(uniques):
            curr = idx+1+(ctr[val]-1)*(n+1)
            res = max(curr,res)
        return res