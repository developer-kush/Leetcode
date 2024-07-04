# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode()
        curr = res
        head = head.next
        
        while head:
            if head.val == 0:  
                curr.next = ListNode()
                curr = curr.next
            else:
                curr.val += head.val
            head = head.next
        
        curr = res
        while curr:
            if curr.next and curr.next.val == 0:
                curr.next = None
                break
            curr = curr.next
        
        return res