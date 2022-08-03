#brutal force solution
from typing import List
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        def calculate(nums, index, upwards):
            maxcount = 0
            for i in range(index+1, len(nums)):
                if (not upwards and nums[index] > nums[i]) or (upwards  and nums[index] < nums[i]):
                    count = 1 + calculate(nums, i, not upwards)
                    maxcount = count if count > maxcount else maxcount
        
            return maxcount
            
        if len(nums) < 2:
            return len(nums)
        
        return 1+ max(calculate(nums,0, True), calculate(nums, 0 , False) )

sol = Solution()
nums = [0,0]
res = sol.wiggleMaxLength(nums)
print(res)


# dynamic programming

# o(n2)
class Solution1:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        dp_up = [1 for _ in range(len(nums)) ]
        dp_down = [1 for _ in range(len(nums))]
        for i in range(len(nums)):
            for j in range(i):
                if nums[j] > nums[i] and 1 + dp_up[j] > dp_down[j]:
                    dp_down[i] = 1 + dp_up[j]
                
                if nums[j] < nums[i] and 1 + dp_down[j] > dp_up[j]:
                    dp_up[i] = 1 + dp_down[j]
        print(dp_up)
        print(dp_down)
        return max(dp_up[-1], dp_down[-1])
    
        
            


sol = Solution1()
nums = [1,17,5,10,13,15,10,5,16,8]
res = sol.wiggleMaxLength(nums)
print(res)

# ### linear dynamic programming
# class Solution2:
#     def wiggleMaxLength(self, nums: List[int]) -> int:

    