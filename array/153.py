from typing import List
class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if nums[0] < nums[-1]:
            return nums[0]
        else:
            l, r  = 0, len(nums) -1
            while l < r:
                if r - l == 1:
                    return min(nums[r], nums[l])
                m = (l + r) // 2
                if nums[m] > nums[0]:
                    l = m 
                else:
                    r = m


                

nums = [3,4,5,1,2]
sol = Solution()
res = sol.findMin(nums)
print(res)

    

        
