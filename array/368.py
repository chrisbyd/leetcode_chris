from typing import List

class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        dp = [1 for _ in range(len(nums))]
       
        max_index = 0
        max_occ = 1
        nums.sort()
        dp_list = {0: [nums[0]]}
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] % nums[j] == 0 and dp[i] < 1 + dp[j]:
                    dp[i] = 1 + dp[j]
                    dp_list[i] = dp_list[j] + [nums[i]]
                elif i not in dp_list:
                    dp_list[i] = [nums[i]]
            if dp[i] > max_occ:
                max_occ = dp[i]
                max_index = i
    
        return dp_list[max_index]
    
sol = Solution()
nums = [343,49,8,4,2,1]
res = sol.largestDivisibleSubset(nums)
print(res)
        
        






