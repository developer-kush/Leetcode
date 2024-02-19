# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        t1 = deque()
        t2 = deque()

        def rec(root, store):
            if root is None: return
            rec(root.left, store)
            store.append(root.val)
            rec(root.right, store)
        
        rec(root1, t1)
        rec(root2, t2)

        res = []
        while t1 and t2:
            if t1[0] < t2[0]: res.append(t1.popleft())
            else: res.append(t2.popleft())
        while t1: res.append(t1.popleft())
        while t2: res.append(t2.popleft())

        return res