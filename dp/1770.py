from typing import List

## time limit exceeded
class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
       ## @lru_cache(None)
        def dp(i, j, k):
            if k == len(multipliers) - 1:
                return max(multipliers[k] * nums[i], multipliers[k] * nums[j])
            else:
                res1 = multipliers[k] * nums[i] + dp(i+1, j, k+1)
                res2 = multipliers[k] * nums[j] + dp(i, j-1, k+1)
                ans = max(res1, res2)
                return ans
        return dp(0, len(nums)-1, 0)
                

sol = Solution()
nums = [1,2,3]
multipliers = [3,2,1]
res = sol.maximumScore(nums, multipliers)
print(res)

### with dynamic programming
#### memory limit exceeded
class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        cache = {}
        def dp(i, j, k):
            if (i,j,k) not in cache: 
                if k == len(multipliers) - 1:
                    ans = max(multipliers[k] * nums[i], multipliers[k] * nums[j])
                    cache[i,j,k] = ans
                    return ans

                else:
                    res1 = multipliers[k] * nums[i] + dp(i+1, j, k+1)
                    res2 = multipliers[k] * nums[j] + dp(i, j-1, k+1)
                    ans = max(res1, res2)
                    cache[i,j,k] = ans
                    return ans
            else:
                return cache[i, j, k]
        return dp(0, len(nums)-1, 0)
                

sol = Solution()
res = sol.maximumScore(nums, multipliers)
print(res)


### easy dynamic programming solution
class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        n, m = len(nums), len(multipliers)
        dp = [[0]* (m + 1) for _ in range(m+1)]
        for i in range(m-1, -1, -1):
            for left in range(i, -1, -1):
                multi = multipliers[i]
                right_index = left + n - i - 1
                dp[i][left] = max(dp[i+1][left] + nums[right_index] * multi, dp[i+1][left+1] + nums[left] * multi)
        return dp[0][0] 

sol = Solution()
nums = [1,2,3]
multipliers = [3,2,1]
res = sol.maximumScore(nums, multipliers)
print(res)


