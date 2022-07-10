
import heapq

from numpy import ones

### prefix sum solution

class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        psum = [0]
        for i in s:
            psum.append(psum[-1] + int(i))
        
        ans = float('inf')
        for j in range(len(psum)):
            cur = psum[j] + len(s) - j - (psum[-1] - psum[j])
            ans = min(ans, cur)
        return ans


sol = Solution() 
s = "00110"
s = "010110"
res = sol.minFlipsMonoIncr(s)
print(res)


        
        

###solution 1 D dp
class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        dp = [0 for i in range(len(s)+1)]
        ones_count = 0
        for i, digit in enumerate(s): 
            if int(digit) == 0:
                ans = min(ones_count, dp[i] + 1)
                dp[i+1] = ans
            elif int(digit) == 1:
                dp[i+1] = dp[i]
                ones_count += 1
        return dp[-1]


sol = Solution() 
s = "00110"
s = "010110"
res = sol.minFlipsMonoIncr(s)
print(res)






        




###solution 2D dp  divide and conquer
class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        pass











        




        