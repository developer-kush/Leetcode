# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:

        def rec(root,val):
            if root.left==None and root.right==None:
                return val*10+root.val
            tot=0
            if root.left!=None: tot+=rec(root.left,val*10+root.val)
            if root.right!=None: tot+=rec(root.right,val*10+root.val)
            return tot
        
        return rec(root,0)