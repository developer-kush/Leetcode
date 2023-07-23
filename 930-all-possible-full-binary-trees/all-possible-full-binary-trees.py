# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        if not n&1: return []
        
        trees = { 1: [TreeNode(0)] }

        for i in range(3, n+1, 2):
            trees[i] = []

            for x in range(1, i, 2):
                y = i-x-1

                for node1 in trees[x]:
                    for node2 in trees[y]:
                        trees[i].append(TreeNode(0, node1, node2))

        return trees[n]