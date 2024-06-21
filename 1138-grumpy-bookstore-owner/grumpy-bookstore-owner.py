class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        tot = sum(customers[i] for i in range(len(customers)) if not grumpy[i])

        mx = curr = l = 0
        for r in range(len(customers)):
            if grumpy[r]: curr += customers[r]
            while r - l >= minutes: 
                if grumpy[l]: curr -= customers[l]
                l += 1
            mx = max(mx, curr)

        return tot + mx