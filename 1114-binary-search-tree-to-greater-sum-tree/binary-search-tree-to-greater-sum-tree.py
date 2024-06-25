# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        def rec(root,val=0):
            if root == None:  return val
            root.val+=rec(root.right,val)
            return rec(root.left,root.val)
        rec(root)
        return root