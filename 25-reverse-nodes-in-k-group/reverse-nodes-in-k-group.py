# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        res, cnt = ListNode(0), 0
        resptr = res
        
        rev = None
        
        while head:

            if cnt and cnt % k == 0:
                while resptr.next: resptr = resptr.next
                resptr.next = rev
                rev = None
            
            next = head.next
            head.next = rev
            rev = head
            head = next
            cnt += 1

        if rev:
            if cnt%k!=0:
                ptr = None
                while rev:
                    next = rev.next
                    rev.next = ptr
                    ptr = rev
                    rev = next
                rev = ptr

            while resptr.next: resptr = resptr.next
            resptr.next = rev
        
        return res.next