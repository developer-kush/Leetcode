# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        par1 = dict()
        par2 = dict()

        def rec(root, par, p=-1):
            if root is None: return
            par[root.val] = p
            rec(root.left, par, root.val)
            rec(root.right, par, root.val)
        
        rec(root1, par1)
        rec(root2, par2)
        return par1 == par2