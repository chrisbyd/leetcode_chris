
# my stupid solution
class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        carry = 0
        ans = 0
        sign = -1 if numerator * denominator < 0 else 1 
        for digit in str(numerator):
            if digit.isdigit():
                res = carry * 10 + int(digit)
                tp = res // abs(denominator)
                ans = ans* 10 + tp
                carry = res % abs(denominator)
        ans = str(ans)
        if ans == "" and carry != 0:
            ans += '0.'
        elif ans == '' and carry == 0:
            ans = '0'
        elif carry != 0:
            ans += '.'
        frac = []
        repeat_set = []
        while carry != 0:
            repeat_set.append(carry)
            carry = carry * 10
            f = carry // abs(denominator)
            frac.append(str(f))
            carry = carry % abs(denominator)
            if carry in repeat_set:
                break
       
        if carry != 0:
            brac_index = repeat_set.index(carry)
            frac.insert(brac_index, '(')
            ans = ans + ''.join(frac) + ')'
        else: 
            ans = ans + ''.join(frac)
        if sign == -1:
            ans = '-' + ans
        return ans

sol = Solution() 
numerator = -22
denominator = 2
res = sol.fractionToDecimal(numerator, denominator)
print(res)


# a much faster solution
