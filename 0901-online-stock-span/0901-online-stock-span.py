class StockSpanner:

    def __init__(self):
        self.span=[]
    def next(self, price: int) -> int:
        count=1
        while self.span and self.span[-1][1]<=price:
            count+=self.span[-1][0]
            self.span.pop() 
        self.span.append((count,price))
        return count

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)