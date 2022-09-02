from typing import List

class Solution:
    def kthPalindrome(self, queries: List[int], intLength: int) -> List[int]:
        n = intLength // 2 if intLength % 2 == 0 else intLength //2 + 1
        maxnum = 10 ** n - 10 ** (n-1)
        ans = []
        def reverse(num):
            digits = []
            while num:
                digits.append(num % 10)
                num = num // 10
            return digits
        for query in queries:
            if query > maxnum:
                ans.append(-1)
            else:
                res = 10 ** (n-1) + (query -1)
                digits = reverse(res) if intLength % 2 == 0 else reverse(res)[1:]
                for digit in digits:
                    res = res * 10 + digit    
                ans.append(res)
        return ans

sol  = Solution()
queries = [1,2,3,4,5,90]
intLength = 3
queries = [2,4,6]
intLength = 4
res = sol.kthPalindrome(queries, intLength)
print(res)