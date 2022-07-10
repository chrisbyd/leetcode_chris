from typing import List
from unittest import result


# a super easy solution to this problem
# ali 的人这么装逼的吗

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        hmap = {1: 'A', 2: 'B', 3:'C', 4:'D', 5:"E", 6:'F', 7:'G', 8: 'H', 9:'I', 10:'J', 11:'K', 12:'L', 13:'M', 14:'N', 15:'O', 16:'P',
        17:'Q', 18:'R', 19: "S", 20:'T', 21:'U', 22:'V', 23:'W', 24:'X', 25:'Y', 26:'Z'}
        ans = ''
        while columnNumber != 0:
            divide = columnNumber // 26
            left = columnNumber % 26
            if left == 0:
                left = 26
                ans += hmap[left]
                columnNumber = divide -1
            else:
                ans += hmap[left]
                columnNumber = divide
        return ans[::-1]


         

sol = Solution()
num = 701
res = sol.convertToTitle(num)
print(res)

# a standard better solution

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = ''
        while columnNumber:
           columnNumber -= 1
           charValue = columnNumber % 26
           columnNumber //= 26
           result = chr(charValue + ord('A')) + result
           
        return result


sol = Solution()
num = 701
res = sol.convertToTitle(num)
print(res)