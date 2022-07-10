from turtle import left
from typing import List
from unittest import result


# it doesnot contain spaces
class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        stack = []
        memo = {}
        def helper(s, i, j):
            if (i,j) in memo:
                return memo[i,j]
            
            if s[i].isdigit() and (i == j or i + 1 == j):
                if i == j:
                    return [int(s[i])]
                else:
                    return [int(s[i:j+1])]

                
            result = []
            for idx in range(i, j+1):
                if not s[idx].isdigit():
                    left_express = helper(s, i, idx-1)
                    right_express = helper(s, idx+1, j)
                    for lr in left_express:
                        for ri in right_express:
                            if s[idx] == '+': result.append(lr + ri)
                            if s[idx] == '-': result.append(lr - ri)
                            if s[idx] == '*': result.append(lr * ri)
            memo[i,j] = result
            return result
        return helper(expression, 0, len(expression) - 1)

sol = Solution()
expression = "2-1-1"
res = sol.diffWaysToCompute(expression)
print(res)