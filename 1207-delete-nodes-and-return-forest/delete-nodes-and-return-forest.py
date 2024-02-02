# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        
        to_delete = set(to_delete)
        res = []
        if root.val not in to_delete: res.append(root)

        def rec(root, rem = False):
            if root is None: return

            left, right = root.left, root.right

            if left is not None and left.val in to_delete: root.left = None
            elif rem and left: res.append(left)

            if right is not None and right.val in to_delete: root.right = None
            elif rem and right: res.append(right)

            rec( left, left is not None and left.val in to_delete )
            rec( right, right is not None and right.val in to_delete )
        
        rec(root, root.val in to_delete)

        return res