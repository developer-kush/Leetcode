# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestPerfectSubtree(self, root: Optional[TreeNode], k: int) -> int:

        res = []

        def rec(root):
            nonlocal res
            if root is None: return [0, 0] # Depth, Children
            d1, c1 = rec(root.left)
            d2, c2 = rec(root.right)

            nd = max(d1, d2) + 1
            nc = c1 + c2 + 1

            if nc == (1<<nd)-1: res.append(nc)

            return [nd, nc]

        rec(root)
        
        if len(res) < k: return -1
        return sorted(res)[-k]