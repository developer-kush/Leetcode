class Solution:
    def maxLength(self, arr: List[str]) -> int:
        def uniq(s):
            return len(s)==len(set(i for i in s))
        arr=[set(j for j in i) for i in arr if uniq(i)]
        curr=set()
        def rec(pos,curr):
            if pos <0: return 0
            if len(curr.intersection(arr[pos])):
                return rec(pos-1,curr)
            
            res=rec(pos-1,curr)
            for i in arr[pos]: curr.add(i)
            res=max(res,rec(pos-1,curr)+len(arr[pos]))
            for i in arr[pos]: curr.remove(i)
            
            return res
        return rec(len(arr)-1,curr)