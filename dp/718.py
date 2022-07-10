from functools import lru_cache
from typing import List

#### not correct! sub array must be contigious
class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        m, n = len(nums1), len(nums2)
        def dp(i, j):
            if i == -1:
                return 0
            elif j == -1:
                return 0
            elif nums1[i] == nums2[j]:
                return 1 + dp(i-1, j-1)
            else:
                return max(dp(i-1, j), dp(i, j-1))
        return dp(m-1, n-1)

sol = Solution()
nums1 = [1,2,3,2,1]
nums2 = [3,2,1,4,7]
nums1 = [0,1,1,1,1]
nums2 = [1,0,1,0,1]
res = sol.findLength(nums1, nums2)
print(res)


# Still TLE error but it is correct
class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        m, n = len(nums1), len(nums2)
        @lru_cache(None)
        def dp(i, j, length):
            if i == m:
                return length
            elif j == n:
                return length
            elif  nums1[i] == nums2[j]:
                return max(dp(i+1, j+1, length +1), dp(i+1,j, 0), dp(i, j+1, 0)) 
            else:
                return max(length, dp(i+1, j, 0), dp(i, j+1, 0))
        return dp(0, 0, 0)

                

sol = Solution()
nums1 = [1,2,3,2,1]
nums2 = [3,2,1,4,7]
nums1 = [0,1,1,1,1]
nums2 = [1,0,1,0,1]
nums1 = [0,0,0,0,0,0,1,0,0,0]
nums2 = [0,0,0,0,0,0,0,1,0,0]
res = sol.findLength(nums1, nums2)
print(res)


# with the dynamic programming approach from the answer
# let dp[i][j] be the loggest common prefix of nums1[i:] and nums2[j:]
class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        m, n = len(nums1), len(nums2)
        dp = [[0 for j in range(n+1)] for i in range(m+1)]
        for i in range(m-1, -1, -1):
            for j in range(n):
                if nums1[i] == nums2[j]:
                    dp[i][j] = 1 + dp[i+1][j+1]
                else: 
                    dp[i][j] = 0
        ans = 0
   
        for dp_line in dp:
            ans = max(ans, max(dp_line))
        return ans



class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        m, n = len(nums1), len(nums2)
        dp = [[0 for j in range(n+1)] for i in range(m+1)]
        for i in range(m-1, -1, -1):
            for j in range(n):
                if nums1[i] == nums2[j]:
                    dp[i][j] = 1 + dp[i+1][j+1]
                else: 
                    dp[i][j] = 0
        ans = 0
   
        return max(max(row) for row in dp)
        

sol = Solution()
nums1 = [1,2,3,2,1]
nums2 = [3,2,1,4,7]
nums1 = [0,1,1,1,1]
nums2 = [1,0,1,0,1]
nums1 = [0,0,0,0,0,0,1,0,0,0]
nums2 = [0,0,0,0,0,0,0,1,0,0]
res = sol.findLength(nums1, nums2)
print(res)   





