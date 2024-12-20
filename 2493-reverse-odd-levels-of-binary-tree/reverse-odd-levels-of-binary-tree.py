# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        valdict={}
        
        def rec(root,level):
            if root is None:
                return
            if level&1:
                if level not in valdict:
                    valdict[level]=[]
                valdict[level].append(root.val)
            rec(root.left,level+1)
            rec(root.right,level+1)
        rec(root,0)
        
        for i in valdict:
            valdict[i]= valdict[i][::-1]
        
        begindict={}
        def rec2(root,idx=0,lvl=0):
            if root is None: return
            if lvl&1:
                if lvl not in begindict:
                    begindict[lvl]=idx
                root.val=valdict[lvl][idx-begindict[lvl]]
            rec2(root.left,2*idx+1,lvl+1)
            rec2(root.right,2*idx+2,lvl+1)
                
        rec2(root)
        return root
    
        