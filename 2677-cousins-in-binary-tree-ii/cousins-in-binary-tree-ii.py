# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        lvlsums = {}
        def rec(root,lvl = 0):
            if root is None: return
            lvlsums[lvl] = lvlsums.get(lvl,0) + root.val
            rec(root.left, lvl+1)
            rec(root.right, lvl+1)
        rec(root)
        def rec(root, lvl = 0):
            if root.left is None and root.right is None: return
            currsum = (root.left.val if root.left else 0) + (root.right.val if root.right else 0)
            if root.left: 
                root.left.val = lvlsums[lvl+1]-currsum
                rec(root.left, lvl+1)
            if root.right : 
                root.right.val = lvlsums[lvl+1]-currsum
                rec(root.right, lvl+1)
        rec(root)
        root.val = 0
        return root