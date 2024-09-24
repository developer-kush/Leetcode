class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        prefixes = set()
        for num in arr1:
            num = str(num)
            curr = ""
            for i in range(len(num)):
                curr += num[i]
                prefixes.add(curr)
        
        res = 0
        for num in arr2:
            num = str(num)
            curr = num[:res]
            for i in range(res, len(num)):
                curr += num[i]
                if curr in prefixes:
                    res = max(res, len(curr))
        
        return res