from typing import List


class Solution:
    def isHappy(self, n: int) -> bool:
        def getSquareDigitsSum(num):
            ans = 0
            while num != 0:
                digit = num % 10
                num = num // 10
                ans += digit ** 2
            return ans
            
        hmap = set()
        while n not in hmap:
            if n == 1:
                return True
            else:
                print(n)
                hmap.add(n)
                n = getSquareDigitsSum(n)
        return False

sol = Solution() 
n = 19
res = sol.isHappy(n)
print(res)