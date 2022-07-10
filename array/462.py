from typing import List

#python sorting problem
class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        pass






        

class Solution:
    def minMoves2(self, nums):
        nums.sort()
        mid = len(nums) // 2
        ans = 0
        for num in nums:
            ans += abs(num - nums[mid])
        return ans
 

sol = Solution()
nums = [1,0,0,8,6]
res = sol.minMoves2(nums)
print(res)
       

