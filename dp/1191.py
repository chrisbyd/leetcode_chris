
from typing import List
class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        n = len(arr)
        dp = arr.copy()
        for i in range(1, n):
            dp[i] = max(dp[i-1] + arr[i], arr[i])
        dp2_right, dp2_left = arr.copy(), arr.copy()
        for i in range(1, n):
            dp2_left[i] = arr[i] + dp2_left[i-1]
        for i in range(n-2, -1, -1):
            dp2_right[i] = arr[i] + dp2_right[i+1]
        max_k1 = max(dp)
        max_k2 = max(dp2_left) + max(dp2_right)
  
        if k == 1:
            return max_k1 % (10 ** 9+ 7) if max_k1 >= 0 else 0
        if max_k2 <= max_k1:
            return  max_k1 % (10 ** 9+ 7) if max_k1 >= 0 else 0
        else:
            if sum(arr) <=  0:
                return max_k2 % (10 ** 9 + 6)
            else:
                return (max_k2 + (k-2)* sum(arr)) % (10 ** 9 + 7)

sol = Solution()
arr = [-7,-1,5,2,3,-7,-6,1]
k = 6
arr = [-9,13,4,-16,-12,-16,3,-7,5,-16,16,8,-1,-13,15,3]
k = 6
res = sol.kConcatenationMaxSum(arr, k)
print(res)


#### the solution from discussion
from typing import List
class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        def maxKaden(k):
            ans, cur = 0, 0
            for _ in range(k):
                for num in arr:
                    cur = max(cur + num, num)
                    ans = max(ans, cur)
            return ans
        if k > 2:
            return (max(0, sum(arr)) * (k-2) + maxKaden(2)) % (10 **9 +7)
        else:
            return (maxKaden(k)) % (10 ** 9 +7)





sol = Solution()
arr = [-7,-1,5,2,3,-7,-6,1]
k = 6
arr = [-9,13,4,-16,-12,-16,3,-7,5,-16,16,8,-1,-13,15,3]
k = 6
res = sol.kConcatenationMaxSum(arr, k)
print(res)
#### the solution from discussion
from typing import List
class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        def maxKaden(k):
            ans, cur = 0, 0
            for _ in range(k):
                for num in arr:
                    cur = max(cur + num, num)
                    ans = max(ans, cur)
            return ans
        return ( max(0, k-2) * max(sum(arr), 0) + maxKaden(min(k, 2)) ) % (10 **9 +7)

sol = Solution()
arr = [-7,-1,5,2,3,-7,-6,1]
k = 6
arr = [-9,13,4,-16,-12,-16,3,-7,5,-16,16,8,-1,-13,15,3]
k = 6
res = sol.kConcatenationMaxSum(arr, k)
print(res)