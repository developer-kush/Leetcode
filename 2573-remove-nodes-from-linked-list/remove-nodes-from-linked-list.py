# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:

        def rec(node): # -> [max, NODE]
            if node is None: return
            nxt = rec(node.next)
            if nxt is None: return node


            if node.val < nxt.val:
                return nxt
            else:
                node.next = nxt
                return node
        
        return rec(head)