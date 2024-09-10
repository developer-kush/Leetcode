# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def getGCD(a, b):
            while b:
                a, b = b, a%b
            return a
        
        ptr = head
        while ptr.next:
            gcd = getGCD(ptr.val, ptr.next.val)
            ptr.next = ListNode(gcd, ptr.next)
            ptr = ptr.next.next
        return head