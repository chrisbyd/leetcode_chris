
from typing import List

class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return 0
        ans = [0 for i in range(len(nums))]
        for i in range(2, len(nums)):
            if nums[i] - nums[i-1] == nums[i-1] - nums[i-2]:
                ans[i] = ans[i-1] + 1
        return sum(ans)

sol = Solution()
nums = [1,2,3,4,7,9,11,13]
res = sol.numberOfArithmeticSlices(nums)
print(res)


        