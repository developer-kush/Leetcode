# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def rec(root,mx,mn):
            if root == None: return 0
            mx,mn = max(mx,root.val),min(mn,root.val)
            return max([max(mx-root.val,root.val-mn),rec(root.left,mx,mn),rec(root.right,mx,mn)])
        
        return rec(root,root.val,root.val)