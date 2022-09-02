class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        x = abs(x)
        digits = []
        while x:
            digit = x % 10
            digits.append(digit)
            x  = x // 10
        ans = 0
        for digit in digits:
            if ans > (2 ** 31 -1 ) // 10:
                return 0
            elif ans == (2 ** 31 - 1) // 10 and sign == 1 and digit > 7:
                return 0
            elif ans == (2** 31) // 10 and sign == -1 and digit > 8:
                return 0
            else:
                ans = ans * 10 + digit
        return sign * ans
            
            
            
        