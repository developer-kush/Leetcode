# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def rec(root):
            if root is None: return 0
            return rec(root.left)+rec(root.right)+(root.val if low<=root.val<=high else 0)
        return rec(root)