from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res = (digits[-1] + 1) % 10
        carry = (digits[-1] + 1) // 10
        ans = [res]
        for i in range(len(digits) -2, -1, -1):
            res = (digits[i] + carry) % 10
            carry = (digits[i] + carry) // 10
            ans.append(res)
        if carry != 0:
            ans.append(carry)
        ans = ans[::-1]
        return ans
    
sol = Solution()
digits = [4,3,9,9]
res = sol.plusOne(digits)
print(res)




        