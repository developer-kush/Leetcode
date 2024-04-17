# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        nodeVal={}
        def rec(root,s=""):
            if root.left is None and root.right is None:
                return chr(root.val+97)+s
            if root.left is None: return rec(root.right,chr(97+root.val)+s)
            if root.right is None: return rec(root.left,chr(97+root.val)+s)
            
            return min(rec(root.left,chr(97+root.val)+s),rec(root.right,chr(97+root.val)+s))
        return rec(root)
    