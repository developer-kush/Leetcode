# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        prev, mode = 0, 1
        queue = deque([root,'#'])
        while len(queue)>1:
            curr = queue.popleft()
            if curr == '#': 
                mode = 1-mode
                prev = 0 if mode else inf
                queue.append('#')
                continue
            if curr.val&1!=mode: return False

            if mode and curr.val<=prev: return False
            if not mode and curr.val>=prev: return False
            if curr.left is not None: queue.append(curr.left)
            if curr.right is not None: queue.append(curr.right)
            prev = curr.val
        return True

                
