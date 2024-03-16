# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        extraHead = ListNode(None)
        curr = extraHead

        nxt = None

        while head and head.next:
            first = head
            second = head.next
            nxt = head.next.next

            curr.next = second
            second.next = first
            curr = first
            head = nxt
        
        curr.next = head

        return extraHead.next