
### result in tle
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        divid = abs(dividend)
        divis = abs(divisor)
        ans = 0
        while divid - divis >=0:
            ans += 1
            divid -= divis
        if (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0):
            ans = - ans
        if ans < - 2** 31: ans = - 2**31
        if ans > 2 ** 31 - 1: ans = 2**31 - 1
        return ans

## with bit manipulation
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == - 2 ** 31 and divisor == -1:  return 2**31 - 1
        sign = -1 if (dividend < 0 and divisor > 0) or (dividend >0 and divisor <0) else 1
        a  = abs(dividend)
        b = abs(divisor)
        res = 0
        for i in range(31, -1, -1):
            if (a >> i )- b >= 0 :
                print(a)
                res += (1 << i)
                a = a  -  ( b << i )
        return sign * res
        