
# brutal force solution
class Solution:
    def rotatedDigits(self, n: int) -> int:
        def getDigits(number):
            res = []
            while number != 0:
                digit = number % 10
                number = number // 10 
                res.append(digit)
            return res
        valid_digit = {0, 1, 2, 5, 6, 8, 9}
        count = 0
        for i in range(1, n+1):
            digits = getDigits(i)
            valid = False
            for digit in digits:
                if digit not in valid_digit:
                    valid = False
                    break
                elif digit in {2, 5, 6, 9}:
                    valid = True
            if valid:
                print(i)
                count += 1
        return count

sol = Solution()
n = 857
res = sol.rotatedDigits(n)
print(res)



            



        