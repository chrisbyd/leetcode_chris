from typing import List

# i still could not solve it in a fast way
# a same question since I have resolved before 
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        dp_up = [1 for i in range(len(nums))]
        dp_down = [1 for i in range(len(nums))]
        direction = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                dp_up[i] = dp_down[i-1] + 1
                dp_down[i] = dp_down[i-1]
            elif nums[i] < nums[i-1]:
                dp_down[i] = dp_up[i-1] + 1
                dp_up[i] = dp_up[i-1]
            else:
                dp_down[i] = dp_down[i-1]
                dp_up[i] = dp_up[i-1]
        return max(dp_down[-1], dp_up[-1])
            
sol = Solution()
nums = [1,7,4,9,2,5]
res = sol.wiggleMaxLength(nums)
print(res)


## solution with top_down dynamic programming


class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int: