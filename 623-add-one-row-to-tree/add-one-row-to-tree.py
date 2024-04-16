# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth==1:
            return TreeNode(val,root)
        def rec(root,d):
            if root is None: return 
            if d==depth-1:
                root.left=TreeNode(val,root.left)
                root.right=TreeNode(val,None,root.right)
                return
            rec(root.left,d+1)
            rec(root.right,d+1)
        rec(root,1)
        return root