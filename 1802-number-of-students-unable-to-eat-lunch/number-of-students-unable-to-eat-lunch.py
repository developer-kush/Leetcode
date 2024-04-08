class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        ctr = Counter(students)
        next0 = ctr[0]+1
        next1 = ctr[1]+1
        res = len(students)
        
        for idx, val in enumerate(sandwiches):
            if sandwiches[idx] == 0: next0 -= 1
            if sandwiches[idx]==1: next1 -= 1
            if not next0: res = min(res, idx)
            if not next1: res = min(res, idx)

        return max(0, len(students)-res)