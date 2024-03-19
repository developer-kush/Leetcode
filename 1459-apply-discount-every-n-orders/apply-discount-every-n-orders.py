class Cashier:

    def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):
        self.price = {x: y for x, y in zip(products, prices)}
        self.n = n 
        self.disc = discount
        self.customer = 0

    def getBill(self, product: List[int], amount: List[int]) -> float:
        self.customer = (self.customer + 1) % self.n
        tot = sum(self.price[x]*y for x, y in zip(product, amount))
        if self.customer == 0: return tot * (100-self.disc) / 100
        return tot

# Your Cashier object will be instantiated and called as such:
# obj = Cashier(n, discount, products, prices)
# param_1 = obj.getBill(product,amount)