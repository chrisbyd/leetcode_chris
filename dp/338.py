from typing import List
import math
class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0 for i in range(n+1)]
        if n == 0:
            return [0]
        elif n == 1:
            return [0, 1]
        ans[1] = 1
        subtract =  0
        for i in range(2, n+1):
            if int(math.log2(i)) == math.log2(i):
                subtract = i
            ans[i] = 1 + ans[i - subtract]

        
        return ans

sol = Solution()
n = 8
res = sol.countBits(n)
print(res)


        