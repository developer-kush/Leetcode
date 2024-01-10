# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        
        tree = defaultdict(list)
        
        def rec(root):
            if root is None: return
            if root.left:
                tree[root.val].append(root.left.val)
                tree[root.left.val].append(root.val)
            if root.right:
                tree[root.val].append(root.right.val)
                tree[root.right.val].append(root.val)
            rec(root.left)
            rec(root.right)

        rec(root)

        visited = set([start])

        def rec(root, dist = 0):
            res = dist
            for ne in tree[root]:
                if ne not in visited: 
                    visited.add(ne)
                    res = max(res, rec(ne, dist+1))
            return res

        return rec(start)