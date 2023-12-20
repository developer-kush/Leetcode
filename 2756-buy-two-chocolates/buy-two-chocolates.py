class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices.sort()
        return money if sum(prices[:2])>money else money - sum(prices[:2])