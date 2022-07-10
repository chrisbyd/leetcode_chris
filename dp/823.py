from typing import List
import math
class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        arr.sort()
        dp = [1]* (len(arr))
        s = {value: index for index, value in enumerate(arr)}
     
        for i in range(1, len(arr)):
            ans = 0
            for j in range(i):
                if arr[i] % arr[j] == 0 and arr[i] // arr[j] in s:
                    ans += dp[j] * dp[s[arr[i] // arr[j]]]
            dp[i] += ans 
      
        return int(sum(dp) % (math.pow(10,9) + 7))

sol = Solution()
arr = [2,4]
arr = [2,4,5,10]

res = sol.numFactoredBinaryTrees(arr)
print(res)

                    


            

        