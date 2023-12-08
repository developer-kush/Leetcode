# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        res=[]
        def rec(root):
            res.append(str(root.val))
            if root.left:
                res.append('(')
                rec(root.left)
                res.append(')')
            elif root.right:
                res.append('()')
            if root.right:
                res.append('(')
                rec(root.right)
                res.append(')')
        rec(root)
        return "".join(res)