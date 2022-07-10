from itertools import zip_longest
import typing


from typing import List

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = a[::-1]
        b = b[::-1]
        carry = 0
        ans = []
        for d1, d2 in zip_longest(a, b, fillvalue= 0):
            add = int(d1) + int(d2) + carry
            res = add % 2
            carry = add // 2
            ans.append(res)
        if carry != 0:
            ans.append(carry)
        ans = ans[::-1]
        return "".join(str(d) for d in ans)


sol = Solution()
a = "1010"
b = "1011"
res = sol.addBinary(a, b)
print(res)