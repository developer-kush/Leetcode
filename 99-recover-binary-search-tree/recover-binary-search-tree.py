# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        inorder = []
        def rec(root):
            nonlocal inorder
            if root is None: return
            rec(root.left)
            inorder.append(root.val)
            rec(root.right)
        rec(root)

        inorder.sort()

        ptr = 0
        def rec(root):
            nonlocal ptr, inorder
            if root is None: return 
            rec(root.left)
            root.val = inorder[ptr]
            ptr += 1
            rec(root.right)
        rec(root)

        return root