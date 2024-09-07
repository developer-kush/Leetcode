# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:

        lst = []
        while head:
            lst.append(head.val)
            head = head.next
        
        path = []
        def rec(root):
            if root is None:
                clst = f",{','.join(map(str, lst))},"
                cpath = f",{','.join(map(str, path))},"
                return clst in cpath
            path.append(root.val)
            if rec(root.left): return True
            if rec(root.right): return True
            path.pop()
            return False
        
        return rec(root)