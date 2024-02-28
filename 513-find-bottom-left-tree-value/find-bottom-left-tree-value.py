# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:

        level, ans = [0], [root.val]

        def rec(root, lvl):
            if root is None: return

            if lvl > level[0]: ans[0] = root.val; level[0] = lvl

            rec(root.left, lvl+1)
            rec(root.right, lvl+1)
        
        rec(root, 0)

        return ans[0]