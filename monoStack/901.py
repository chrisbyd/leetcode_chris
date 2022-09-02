class StockSpanner:

    def __init__(self):
        self.stack = []
        self.index = 0 

    def next(self, price: int) -> int:
        while self.stack and self.stack[-1][1] <= price:
            self.stack.pop()
        if self.stack:
            index = self.stack[-1][0]
            ans = self.index - index
        else:
            ans = 0
       
        self.stack.append((self.index, price))
        self.index += 1
        return ans
            
            

# Your StockSpanner object will be instantiated and called as such:
obj = StockSpanner()
param_1 = obj.next(100)
param_1 = obj.next(80)
print(param_1)
