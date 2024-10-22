# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:

        lvls = []

        def rec(root, lvl = 1):
            if root is None: return
            if len(lvls) < lvl: lvls.append(root.val)
            else: lvls[lvl - 1] += root.val
            rec(root.left, lvl+1)
            rec(root.right, lvl+1)

        rec(root)

        if len(lvls) < k: return -1
        return sorted(lvls)[-k]