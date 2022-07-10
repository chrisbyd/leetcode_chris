from typing import List
# brutal force solution
# with backtracking
# TLE time limit exceeded
# TLE了 需要 dynamic programming
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        def backtrack(index, i, j):
            if index == len(s3) and i == len(s1) and j == len(s2):
                return True
            elif index == len(s3) :
                return False
            elif index != len(s3) and i == len(s1) and j == len(s2):
                return False
            elif index != len(s3) and i != len(s1) and j== len(s2):
                if s3[index] != s1[i]:
                    return False
                else:
                    return backtrack(index+1, i+1, j)
            elif index != len(s3) and i == len(s1) and j != len(s2):
                if s3[index] != s2[j]:
                    return False
                return backtrack(index+1, i,  j+1)
            else:
                if s3[index] != s1[i] and s3[index] != s2[j]:
                    return False
                elif s1[i] == s3[index] and s2[j] != s3[index]:
                    return backtrack(index+1, i+1, j)
                elif s1[i] != s3[index] and s2[j] == s3[index]:
                    return backtrack(index+1, i, j+1)
                else:
                    return backtrack(index+1, i+1, j) or backtrack(index+1, i, j+1)
        return backtrack(0, 0, 0)

sol = Solution()
s1 = "abcdaabb"
s2 = "cbba"
s3 = "abcbbabcdaabb"
res = sol.isInterleave(s1, s2, s3)
print(res)                
            
            

# Standard solution with dynamic programming

class Solution1:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m, n = len(s1), len(s2)
        dp = [[False for j in range(n+1)] for i in range(m+1)]
        if len(s1) + len(s2) != len(s3):
            return False
        dp[0][0] = True 
        for i in range(m):
            if s1[i] == s3[i]:
                dp[i+1][0] = dp[i][0]
            else:
                dp[i+1][0] = False
        for j in range(n):
            if s2[j] == s3[j]:
                dp[0][j+1] = dp[0][j]
            else:
                dp[0][j+1] = False
        
        for i in range(m):
            for j in range(n):
                if  s3[i + j +1] == s1[i] and s3[i+j +1] == s2[j]:
                    dp[i+1][j+1] = dp[i][j+1] or dp[i+1][j]
                elif s3[i+j+1] == s1[i] and s3[i+j+1] != s2[j]:
                    dp[i+1][j+1] = dp[i][j+1]
                elif s3[i+j+1] != s1[i] and s3[i+j+1] == s2[j]:
                    dp[i+1][j+1] = dp[i+1][j]
                else:
                    dp[i+1][j+1] = False
        return dp[m][n]




sol = Solution1()
s1 = "abcdaabb"
s2 = "cbba"
s3 = "abcbbacdaabb"
res = sol.isInterleave(s1, s2, s3)
print(res)     

        