class Solution:
    def minAnagramLength(self, s: str) -> int:

        def egcd(a, b):
            while b: a, b = b, a%b
            return a

        ctr = Counter(s)
        gcd = ctr[s[0]]
        for val in ctr.values(): gcd = egcd(gcd, val)

        return sum(val//gcd for val in ctr.values())