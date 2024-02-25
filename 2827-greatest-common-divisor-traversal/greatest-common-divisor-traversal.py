# class DSU:
#     def __init__(self, n):
        

class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        if len(nums) == 1: return True
        if 1 in nums: return False
        
        allNums = set(nums)
        
        def factors(n):
            st = set([n])
            for i in range(2,int(n**0.5)+1):
                if n%i == 0: st.add(i); st.add(n//i)
            return st
        
        graph = {}
        for i in nums:
            for factor in factors(i):
                allNums.add(factor)
                if factor not in graph: graph[factor] = []
                if i not in graph: graph[i] = []
                graph[i].append(factor)
                graph[factor].append(i)
        
                
        visited = set()
        stack = [nums[0]]
        while stack:
            curr = stack.pop()
            for neigh in graph[curr]:
                if neigh not in visited:
                    visited.add(neigh)
                    stack.append(neigh)
        
        if visited == allNums: return True
        return False