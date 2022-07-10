from typing import List
# not standard solution
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        dp = [1 for _ in range(len(nums))]
        dp_list = {0: [nums[0]]}
        max_occ = 0
        max_index = 0
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] % nums[j] == 0 and 1+ dp[j] > dp[i]:
                    dp[i] = 1 + dp[j]
                    dp_list[i] = dp_list[j] + [nums[i] ]
            if i not in dp_list:
                dp[i] = 1
                dp_list[i] = [nums[i]]

            if dp[i] > max_occ: 
                max_occ = dp[i]
                max_index = i
        return dp_list[max_index]

sol = Solution()
nums = [1,2,3,4]
res = sol.largestDivisibleSubset(nums)
print(res)

            

# a more concise solution

class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)
        dp_list = [[nums[i]] for i in range(len(nums))]
        for i in range(n):
            for j in range(i):
                if nums[i] % nums[j] == 0 and len(dp_list[j]) + 1 > len(dp_list[i]):
                    dp_list[i] = dp_list[j] + [nums[i]]
      
        return max(dp_list, key=len)

        
sol = Solution()
nums = [1,2,3,4]
res = sol.largestDivisibleSubset(nums)
print(res)    