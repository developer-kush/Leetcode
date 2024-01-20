class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        arr.insert(0,0)
        n=len(arr)
        res=[0]*n
        stack=[0]

        for i in range(n):
            while len(stack)>1 and arr[stack[-1]]>arr[i]:
                stack.pop()
            j=stack[-1]
            res[i]=(i-j)*arr[i]+res[j]
            stack.append(i)
        return sum(res)%(10**9+7)
