from typing import List

#dynamic programming is so hard!!!!
#The first thing we need to do is to figure out how to set the dp matrix
#dp[m][n] means the max number of units in strs added when there are m zeros and n ones left
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [[-1] *(n+1) for i in range(m+1)]
        dp[-1][-1] = 0

        #O(N*m*n) solution, where $N is the length
        for char in strs:
            num0 = char.count('0')
            num1 = len(char) - num0

            for mm in range(m+1):
                for nn in range(n+1):
                    if dp[mm][nn] >= 0:
                        if mm - num0 >=0 and nn - num1 >= 0:
                            dp[mm - num0][nn- num1] = max(dp[mm- num0][nn - num1], 1 + dp[mm][nn])
        ans = 0
        for i in range(m+1):
            for j in range(n+1):
                ans = max(ans, dp[i][j])
        return ans

sol = Solution()
strs = ["10","0001","111001","1","0"]
m = 5
n = 3
res = sol.findMaxForm(strs, m, n)
print(res)




        