
class MinStack:

    def __init__(self):
        self.stack = []
        self.minimum = []
    
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minimum:
            self.minimum.append(val)
        else:
            self.minimum.append(min(self.minimum[-1], val))
        

    def pop(self) -> None:
        ans =  self.stack.pop()
        self.minimum.pop()
  
        

    def top(self) -> int:
        if  self.stack:
            return self.stack[-1]
        return False
        

    def getMin(self) -> int:
        return self.minimum[-1]
        
        
        

