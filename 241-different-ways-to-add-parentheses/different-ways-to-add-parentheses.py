class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        exp, curr = [], ""
        for i in expression:
            if i in "*+-":
                exp.extend([int(curr),i])
                curr=""
            else: curr+=i
        exp.append(int(curr))

        @lru_cache(4862)
        def rec(lo,hi,memo={}):
            if lo==hi:
                return [exp[lo]]
            result = []
            for i in range(lo+1,hi,2):
                left = rec(lo,i-1)
                right = rec(i+1,hi)
                for x in left:
                    for y in right:
                        result.append(x+y if exp[i]=='+' else x-y if exp[i] =='-' else x*y)
            return result
        
        return rec(0,len(exp)-1)
