# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        srcNode = None
        root.parent = None
        def rec(root):
            nonlocal srcNode, startValue
            if root is None: return 0
            if root.val == startValue: srcNode = root
            if root.left: root.left.parent = root
            if root.right: root.right.parent = root
            rec(root.left)
            rec(root.right)
        rec(root)

        res = ""
        def rec(root, par):
            nonlocal res, destValue
            if root.val == destValue: return True
            for node, char in ((root.left, "L"), (root.right, "R"), (root.parent, "U")):
                if node in (None, par): continue
                if rec(node, root): res += char; return True
            
        rec(srcNode, None)
        return res[::-1]