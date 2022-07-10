from functools import lru_cache
from typing import List

from torch import maximum, minimum
# TLE error
class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        dp = [0 for i in range(len(nums))]
        maximum = minimum = nums[0]
        for i in range(1, len(nums)):
            dp[i] = dp[i-1]
        
            for j in range(i):
                dp[i] += max(nums[j:i+1]) - min(nums[j:i+1])
        return dp[-1]

# sol = Solution()
# nums = [4,-2,-3,4, 1]
# res = sol.subArrayRanges(nums)
# print(res)

# optimized with o(n^2) by storing the largest and smallest as a range. it is accepted
class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        dp = [0 for i in range(len(nums))]
        prev = [[nums[0], nums[0]]]
        for i in range(1, len(nums)):
            ans = 0
            new_prev = []
            for num in prev:
                if nums[i] < num[0]:
                    num[0] = nums[i]
                elif nums[i] > num[1]:
                    num[1] = nums[i]
                ans += num[1] - num[0]
                new_prev.append(num)
            new_prev.append([nums[i], nums[i]])
            prev = new_prev
            dp[i] = dp[i-1] + ans  
        return dp[-1]
sol = Solution()
nums = [4,-2,-3,4, 1]
res = sol.subArrayRanges(nums)
print(res)


#optimized solution with O(N^2) without dynamic programming
class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for i in range(n):
            maxi, mini = nums[i], nums[i]
            for j in range(i+1, n):
                if nums[j] > maxi:
                    maxi = nums[j]
                elif nums[j] < mini:
                    mini = nums[j]
                ans += maxi - mini
        return ans

sol = Solution()
nums = [4,-2,-3,4, 1]
res = sol.subArrayRanges(nums)
print(res)


#optimized O(n) solution with stack
#monotonic stack solution
# class Solution:
#     def subArrayRanges(self, nums: List[int]) -> int:


        