class Solution:
    def countPalindromePaths(self, parent: List[int], s: str) -> int:
        ctr = Counter()

        tree = defaultdict(list)
        for i in range(1, len(parent)):
            tree[parent[i]].append((i, s[i]))
        
        def rec(root, sc):
            res = 0
            for ne, ch in tree[root]:
                res += rec(ne, sc ^ (1<<(ord(ch)-97)))
            res += ctr[sc]
            res += sum(ctr[sc^(1<<i)] for i in range(26))
            ctr[sc] += 1
            return res

        return rec(0, 0)