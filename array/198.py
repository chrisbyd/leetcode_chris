from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:
        def dp(nums):
            if len(nums) == 0:
                return 0
            if len(nums) == 1:
                return nums[0]
            if len(nums) == 2:
                return max(nums)

            res = max(nums[0]+ dp(nums[2:]), nums[1] + dp(nums[3:]))
            return res
        return dp(nums)



nums = [2,7,9,3,1]
sol = Solution()
res = sol.rob(nums)
print(res)

class Solution1:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums[0], nums[1]) 
        maxValue = [0 for _ in range(len(nums))]
        maxValue[0], maxValue[1] = nums[0], max(nums[0], nums[1])
        for i in range(2, len(nums)):
            maxValue[i] = max(maxValue[i-1], nums[i]+ maxValue[i-2])
        return maxValue[-1]

          

nums = [2,7,9,3,1]
sol = Solution１()
res = sol.rob(nums)
print(res)
