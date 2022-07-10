from functools import lru_cache
from typing import List
##### time limit exceeded

#### TLE error
class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        if len(arr) == 2:
            return arr[0] * arr[1]
        def dp(arr):
            if len(arr) == 1:
                return 0
            elif len(arr) == 2:
                return arr[0] * arr[1]
            else:
                ans = float('inf')
                for i in range(1, len(arr)):
                    newValue = dp(arr[:i]) + dp(arr[i:]) + max(arr[:i]) * max(arr[i:])
                    ans = min(ans, newValue)
            return ans
        return dp(arr)



#### with cache
class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        if len(arr) == 2:
            return arr[0] * arr[1]
        @lru_cache(None)
        def dp(start, end):
            if start == end:
                return 0
            elif end - start == 1:
                return arr[end] * arr[start]
            else:
                ans = float('inf')
                for i in range(start, end):
                    newValue =  dp(start, i) + dp(i+1, end) + max(arr[start: i+1]) * max(arr[i+1:end+1])
                    ans = min(ans, newValue)

            return ans
        return dp(0, len(arr)-1)

sol = Solution()
input = [6,2,4,8,7]
res = sol.mctFromLeafValues(input)
print(res)