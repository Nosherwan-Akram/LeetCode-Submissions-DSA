class ProductOfNumbers:

    def __init__(self):
        self.prefixProd = [1]
        
    def add(self, num: int) -> None:
        if num == 0:
            self.prefixProd = [1]
        else:
            self.prefixProd.append(self.prefixProd[-1]*num)

    def getProduct(self, k: int) -> int:
        if k >= len(self.prefixProd):
            return 0
        return self.prefixProd[-1]//self.prefixProd[-k-1]


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)