from typing import List
class Solution:
    def grayCode(self, n: int) -> List[int]:
        def dp(n):
            if n == 1:
                return [0, 1]
            else:
                ans = dp(n-1)
                add = (1 << n-1)
                res =  ans + [i+ add for i in ans[::-1]]
                return res
        return dp(n)
        
        