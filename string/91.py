from typing import List

class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0 for i in range(len(s)+1)]
        dp[1] = 0 if s[0] == '0' else 1
        dp[0] = 1
        for i in range(1, len(s)):
            if s[i] == '0':
                if int(s[i-1: i+1]) > 0 and int(s[i-1: i+1]) < 27:
                    dp[i+1] = dp[i-1]
                else:
                    dp[i+1] = 0
            else:

                if s[i-1] != '0' and int(s[i-1: i+1]) > 0 and int(s[i-1: i+1]) < 27:
                    if s[i] != "0":
                        dp[i+1] = dp[i] + dp[i-1]
                else:
                    if s[i] != '0':
                        dp[i+1] = dp[i]
                    else:
                        dp[i+1] = 0
        return dp[-1]




sol = Solution()
s = '1110'
res = sol.numDecodings(s)
print(res)




        