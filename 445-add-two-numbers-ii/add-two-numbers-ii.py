# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def revlinked(head):
            prev = None
            curr = head
            while curr:
                Nxt = curr.next
                curr.next = prev
                prev = curr
                curr = Nxt
            return prev
            
        carry = 0
        l1 = revlinked(l1)
        l2 = revlinked(l2)
        res = curr = ListNode()
        while carry or l1 or l2:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            curr.next = ListNode(carry%10)
            carry //= 10
            curr = curr.next

        return revlinked(res.next)

