# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        leafSequence1=[]
        leafSequence2=[]
        def rec(root,seq):
            if root.left is None and root.right is None:
                seq.append(root.val)
                return
            if root.left is not None:
                rec(root.left,seq)
            if root.right is not None:
                rec(root.right,seq)
        rec(root1,leafSequence1)
        rec(root2,leafSequence2)
        return leafSequence1 == leafSequence2