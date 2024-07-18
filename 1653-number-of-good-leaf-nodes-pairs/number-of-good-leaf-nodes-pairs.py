# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        if distance == 1: return 0

        def rec(root):
            if root is None: return (0, [0]*10)
            if root.left is None and root.right is None: 
                return (0, [1]+([0]*9))
            x, l = rec(root.left)
            y, r = rec(root.right)
            
            tot = x + y

            psum = list(r)
            for i in range(1, 10): psum[i] += psum[i-1]

            for i in range(distance-1):
                tot += l[i] * psum[distance-2-i]

            for i in range(10): l[i] += r[i]
            l.pop(); l.insert(0, 0)

            return (tot, l)

        return rec(root)[0]