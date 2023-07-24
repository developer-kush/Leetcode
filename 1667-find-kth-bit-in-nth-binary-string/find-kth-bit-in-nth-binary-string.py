class Solution:
    def findKthBit(self, n: int, k: int) -> str:

        ln = (1<<n) - 1

        def rec(k, inv, ln):

            if ln == 1:
                if inv&1: return '1'
                return '0'

            nln = ln>>1
            if k == nln:
                if inv&1: return'0'
                return '1'
            
            if k > nln: return rec(nln+nln-k, inv+1, nln)
            
            return rec(k, inv, nln)

        return rec(k-1, 0, ln)