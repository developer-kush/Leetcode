# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        
        tot = 0

        def rec(root):
            nonlocal tot
            if root is None: return [0, 0]
            lcoins, lchild = rec(root.left)
            rcoins, rchild = rec(root.right)
            tot += abs(lcoins - lchild) + abs(rcoins - rchild)
            return [lcoins + rcoins + root.val, lchild + rchild + 1]

        rec(root)
        return tot