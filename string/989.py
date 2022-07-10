from itertools import zip_longest
from typing import List
class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        if k == 0:
            return num
        k_list = []
        while k != 0:
            k_list.append(k % 10)
            k = k // 10
          
        num = num[::-1]
        carry = 0
        ans = []
        for d1, d2 in zip_longest(num, k_list, fillvalue= 0):
            add = d1 + d2 + carry
            res = add % 10
            carry = add // 10
            ans.append(res)
        if carry != 0:
            ans.append(carry)
        return ans[::-1]

sol = Solution()
num = [2,1,5]
k = 806
res = sol.addToArrayForm(num, k)
print(res)


        