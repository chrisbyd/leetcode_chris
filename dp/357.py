# a solution by myself


# my solution
class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        dp = [0 for i in range(n+1)]
        dp[0] = 1
        product = [0 for i in range(n+1)]
        mul = 9
        res = 1
        for i in range(1, n+1):
            if mul == 0:
                product[i] = 0
            else:
                res = mul * res
                product[i] = res
            if i >= 2:
                mul -= 1
    
        for i in range(1,n+1):
            dp[i] = dp[i-1] + product[i]
        return dp[-1]

sol = Solution()
n = 3
res = sol.countNumbersWithUniqueDigits(n)
print(res)

# optimized solution with less memory
class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        dp = [0 for i in range(n+1)]
        dp[0] = 1
        product = 9
        mul = 9
        for i in range(1,n+1):
            dp[i] = dp[i-1] + product
            product = product * mul 
            mul = max(0, mul - 1)

        return dp[-1]

sol = Solution()
n = 3
res = sol.countNumbersWithUniqueDigits(n)
print(res)
