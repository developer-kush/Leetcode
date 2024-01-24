# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        
        def rec(root,cnt=0):
            if root is None: return 0
            cnt^= (1<<root.val)
            if root.left is None and root.right is None:
                if cnt==0 or cnt&-cnt==cnt:
                    return 1
                else: return 0
            return rec(root.left,cnt)+rec(root.right,cnt)
            
        return rec(root)