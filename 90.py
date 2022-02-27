from typing import List
# class Solution:
#     def getSub(self, nums, count, current_set, res):
#         if count == len(current_set):
#             res.append(current_set[:])
#             return res
#         else:
#             for num in set(nums):
#                 print(nums)
#                 nums.remove(num)
#                 current_set.append(num)
#                 self.getSub(nums, count, current_set, res)
#                 current_set.remove(num)
#                 nums.append(num)
#                 print(nums)
              

#     def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
#         res = []
#         for count in range(len(nums),-1,-1):
#             self.getSub(nums, count, [], res)
#         return res


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
               
        result = []
        nums.sort()
        def backtrack(current, index):
            if index >= len(nums):
                result.append(current)
            else:
                backtrack(current + [nums[index]], index + 1)
                while index < len(nums)-1 and nums[index] == nums[index+1]:
                    index +=1
                backtrack(current, index+1)
        backtrack([], 0)
        return result



sol = Solution()

nums = [1,2,2]
result = sol.subsetsWithDup(nums)
print(result)

class Solution1:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

               
        