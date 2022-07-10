from itertools import zip_longest
from typing import List
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        num1 = num1[::-1]
        num2 = num2[::-1]
        carry = 0
        ans = ""
        for d1, d2 in zip_longest(num1, num2, fillvalue= 0):
            add = int(d1) + int(d2) + carry
            res = add % 10
            carry = add // 10
            ans += str(res)
        
        if carry != 0:
            ans += str(carry)
   
        return ans[::-1]

sol = Solution()

num1 = "456"
num2 = "77"
res = sol.addStrings(num1, num2)
print(res)
