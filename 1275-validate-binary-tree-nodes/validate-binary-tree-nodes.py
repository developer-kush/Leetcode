class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        src = list(set(list(range(n))+[-1])-set(leftChild+rightChild))
        if len(src) != 1: return False

        visited = set()

        def rec(root):
            if root == -1: return True
            if root in visited: return False
            visited.add(root)
            return rec(leftChild[root]) and rec(rightChild[root])

        return rec(src[0]) and len(visited)==n