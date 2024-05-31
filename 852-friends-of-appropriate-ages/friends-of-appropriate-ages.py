class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        ages.sort()
        tot = 0
        for i in range(len(ages)):
            lower = ages[i]/2+7.1
            upper = ages[i]
            ub = bisect_right(ages, upper)
            lb = bisect_left(ages, lower)
            tot += max(ub - lb - 1, 0)
        return tot