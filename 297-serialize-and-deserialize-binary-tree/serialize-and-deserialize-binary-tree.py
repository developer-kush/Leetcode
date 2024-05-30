# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# TreeNode.__repr__ = lambda self : f"{self.val} [{self.left}, {self.right}]"

class Codec:

    def serialize(self, root):
        res = ""
        def rec(root):
            nonlocal res
            if root is None: 
                res += ";,"
                return
            res += str(root.val)+"," 
            rec(root.left)
            rec(root.right)
            res += ";,"
        rec(root)
        return res.strip(",")

    def deserialize(self, data):
        values = data.split(',')
        pos = 0
        def rec():
            nonlocal pos, values
            if values[pos] == ';': pos += 1; return 
            res = TreeNode(values[pos])
            pos += 1
            res.left = rec()
            res.right = rec()
            if values[pos] == ";": pos += 1
            return res
        return rec()

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))