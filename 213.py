from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        self.length = len(nums)

        def dpCircle(nums):
            if len(nums) < 1:
                return 0
            elif len(nums) == 1:
                return nums[0]
            else:
                return max(dp(nums[:-1]), nums[-1] + dp(nums[1:-2]))

        def dp(nums):
            if len(nums) < 1:
                return 0
            elif len(nums) == 1:
                return nums[0]
            else:
                return max(dp(nums[:-1]), dp(nums[:-2]) + nums[-1])
        
        return dpCircle(nums)

# sol = Solution()

# nums = [1,2,3]
# res = sol.rob(nums)
# print(res)

class Solution1:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]

        dp1 = [0 for i in range(len(nums))]
        dp2 = [0 for i in range(len(nums) - 3)]
        new_nums = nums[1:-2]
      
        for index, _ in enumerate(dp2):
     
            if index == 0:
                dp2[index] = new_nums[index]
            elif index == 1:
                dp2[index] = max(new_nums[:2])
            else:
                dp2[index] = max(new_nums[index] + dp2[index-2], dp2[index -1] )
       
        for index, _ in enumerate(dp1):
            if index == 0:
                dp1[index] = nums[index]
            elif index == 1:
                dp1[index] = max(nums[:2])
            elif index < len(dp1) -1:
                dp1[index] = max(nums[index] + dp1[index-2], dp1[index-1])
            else:
                if len(dp2) < 1:
                    dp1[index] = max(dp1[-2], nums[-1])
                else:
                    dp1[index] = max(dp1[-2], nums[-1] + dp2[-1] )

        return dp1[-1]




sol = Solution1()

nums =  [1,2,3,1]
res = sol.rob(nums)
print(res)




