from filecmp import cmp
from typing import List


### my solution
class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        n = len(arr)
        dp_up   = [1 for i in range(n)]
        dp_down = [1 for i in range(n)]
        direct1, direct2 = 1, 0
        for i in range(1, n):
            if arr[i] > arr[i-1]:
                if direct1 == 1:
                    dp_up[i] = dp_up[i-1] + 1 
                if direct2 == 1:
                    dp_down[i] = dp_down[i-1] +1 
            elif arr[i] < arr[i-1]:
                if direct1 == 0:
                    dp_up[i] = dp_up[i-1] + 1 
                if direct2 == 0:
                    dp_down[i] = dp_down[i-1] +1 
            
            direct1, direct2 = 1 - direct1, 1 - direct2
        return max(max(dp_up), max(dp_down))

sol = Solution()
arr = [9,4,2,10,7,8,8,1,9]
arr = [100]
# arr = [4,8,12,16]
# arr = [2,3,2,4,1]
arr = [9, 9]
res = sol.maxTurbulenceSize(arr)
print(res)


## sliding window algorithm
### It is a pretty good algorithm
####
# class Solution:
#     def maxTurbulenceSize(self, arr: List[int]) -> int:
#         cmp()
        
        
class Solution(object):
    def maxTurbulenceSize(self, arr):
        def cmp(a, b):
            ans = 1 if a > b else (-1 if a < b else 0)
            return ans
        ans = 1
        anchor = 0
        for i in range(1, len(arr)):
            c = cmp(arr[i-1], arr[i])
            if c == 0:
                anchor = i
            elif i == len(arr) -1 or c*cmp(arr[i], arr[i+1]) != -1:
                ans = max(ans, i - anchor + 1)
                anchor = i
        return ans


       

sol = Solution()
arr = [9,4,2,10,7,8,8,1,9]
arr = [100]
# arr = [4,8,12,16]
# arr = [2,3,2,4,1]
arr = [9, 9]
res = sol.maxTurbulenceSize(arr)
print(res)