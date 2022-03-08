from typing import List 

# class Solution:
#     def findPeakElement(self, nums: List[int]) -> int:
#         n = len(nums)
#         for i in range(n-1):
#             if nums[i] > nums[i+1]:
#                 return i
#         return n-1

# sol = Solution()

# nums = [1,2,3,1]
# res = sol.findPeakElement(nums)
# print(res)




class Solution1:
    def findPeakElement(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) // 2
         
            if nums[mid] > nums[mid + 1]:
                r = mid
            else:
                l = mid + 1 
        return l 

sol = Solution1()
nums = [1,2,3,1]
res = sol.findPeakElement(nums)
print(res)

