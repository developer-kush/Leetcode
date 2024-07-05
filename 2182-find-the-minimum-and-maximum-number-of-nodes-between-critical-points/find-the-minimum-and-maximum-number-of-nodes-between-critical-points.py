# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        mindist, maxdist = inf, float('-inf')

        f = l = None
        lastval = head.val
        ctr = 1
        while head.next:
            if lastval > head.val < head.next.val \
                or lastval < head.val > head.next.val:

                if l:
                    mindist = min(mindist, ctr-l)
                    maxdist = max(maxdist, ctr-f)
                if f is None: f = ctr
                l = ctr
            
            lastval = head.val
            ctr += 1
            head = head.next

        if (mindist, maxdist) == (inf, float('-inf')): return [-1, -1]
        return [mindist, maxdist]