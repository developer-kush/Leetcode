# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        
        def rec(root):
            if root is None: return [0, 0, 0]
            sc1, n1, sm1 = rec(root.left)
            sc2, n2, sm2 = rec(root.right)
            return [
                sc1+sc2+int((sm1+sm2+root.val) // (n1+n2+1) == root.val), 
                n1+n2+1, sm1+sm2+root.val
            ]
            
        return rec(root)[0]