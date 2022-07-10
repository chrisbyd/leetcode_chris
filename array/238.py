from typing import List 

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left, right = 1, 1
        output = [1 for _ in range(n)]
        for i in range(n):
            output[i] = left
            left *= nums[i]
        
        for j in range(n-1, -1, -1):
            output[j] *= right
            right *= nums[j]
        
        return output

sol = Solution()
nums = [1,2,3,4]
res = sol.productExceptSelf(nums)
print(res)

        