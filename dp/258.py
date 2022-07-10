
class Solution:
    def addDigits(self, num: int) -> int:
        def digitSum(num):
            ans = 0
            while num != 0:
                digit = num % 10
                num = num // 10
                ans += digit
            return ans
        
        while num >= 10:
            num = digitSum(num)
        return num
        
        