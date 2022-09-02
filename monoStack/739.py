from typing import List
###monotonic stack

class Solution:
    def dailyTemperatures(self, temps: List[int]) -> List[int]:
        n = len(temps)
        ans = [0] * n
        stack = []
        for i in range(n-1, -1, -1):
            while stack and stack[-1][1] <= temps[i]:
                stack.pop()
            if stack:
                date, _ = stack[-1]
                ans[i] = date - i
            stack.append((i, temps[i]))
        return ans
        
        