from typing import List

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for i, digit in enumerate(num):
            while stack and stack[-1] > digit and k > 0:
                stack.pop()
                k -= 1
            if digit != '0' or stack:
                stack.append(digit)
        if k != 0:
            stack = stack[:- k]
        if not stack:
            return '0'
        return ''.join(stack)
            
sol = Solution()
nums = "1432219"
k = 3
res = sol.removeKdigits(nums, k)
print(res)