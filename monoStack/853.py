from typing import List

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pts, n = {} , len(position)
        for i in range(n):
            pts[position[i]] = speed[i]
        position.sort()
        arrival, stack  = [], [] 
        for i in range(n):
            arrival.append((target - position[i]) / pts[position[i]])
        
        for i in range(n):
            while stack and stack[-1] <=  arrival[i]:
                stack.pop()
            stack.append(arrival[i])
        return len(stack)