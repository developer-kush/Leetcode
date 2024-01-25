class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        def rec(a,b,memo={}):
            if (a,b) in memo: return memo[(a,b)]
            if a<0 or b<0: return 0
            if text1[a]==text2[b]: memo[(a,b)] = rec(a-1,b-1,memo)+1
            else: memo[(a,b)] = max(rec(a-1,b,memo),rec(a,b-1,memo))
            return memo[(a,b)]
        return rec(len(text1)-1,len(text2)-1)