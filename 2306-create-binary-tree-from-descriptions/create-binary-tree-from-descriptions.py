# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        st = set()
        st2 = set()
        tree = defaultdict(lambda : [-1, -1])
        for r, c, side in descriptions: 
            tree[r][1-side] = c
            st.add(r)
            st2.add(c)

        def build(root):
            if root == -1: return None
            return TreeNode(
                root,
                build(tree[root][0]),
                build(tree[root][1])
            )
        
        return build(list(st-st2)[0])