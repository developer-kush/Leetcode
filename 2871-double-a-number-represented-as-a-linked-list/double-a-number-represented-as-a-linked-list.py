# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.val == 0: return head
        
        num = 0
        while head:
            num = num*10 + head.val
            head = head.next
        num*=2
        
        res = None
        while num:
            res = ListNode(num%10, res)
            num//=10
        return res