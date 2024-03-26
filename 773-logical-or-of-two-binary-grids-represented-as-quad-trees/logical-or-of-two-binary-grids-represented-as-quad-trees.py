"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def intersect(self, t1: 'Node', t2: 'Node') -> 'Node':
        if t1.isLeaf and t1.val: return t1
        if t2.isLeaf and t2.val: return t2

        def rec(t1, t2):
            if t1.isLeaf:
                if t1.val: return t1
                else: return t2
            if t2.isLeaf:
                if t2.val: return t2
                else: return t1
            
            tl = rec(t1.topLeft, t2.topLeft)
            tr = rec(t1.topRight, t2.topRight)
            bl = rec(t1.bottomLeft, t2.bottomLeft)
            br = rec(t1.bottomRight, t2.bottomRight)

            print(tl.isLeaf, tr.isLeaf, bl.isLeaf, br.isLeaf)

            if tl.isLeaf and tl.val and tr.isLeaf and tr.val and \
                bl.isLeaf and bl.val and br.isLeaf and br.val:
                print("Merged to 1")
                return Node(True, True)
            if tl.isLeaf and not tl.val and tr.isLeaf and not tr.val \
                and bl.isLeaf and not bl.val and br.isLeaf and not br.val:
                print("Merged to 0")
                return Node(True, False)

            return Node(0, False, tl, tr, bl, br)

        return rec(t1, t2)