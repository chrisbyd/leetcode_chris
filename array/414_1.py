from typing import List

# class Solution:
#     def thirdMax(self, nums: List[int]) -> int:
#         count = 0
#         memo = set()
#         for num in nums:
#             if num not in memo:
#                 count += 1
#                 memo.add(num)
#                 if count == 3:
#                     return num
#         return max(nums)
        
# sol = Solution() 
# nums = [3,2,1]
# res = sol.thirdMax(nums)
# print(res)
class Solution:
    def thirdMax(self, nums):
        count = 0
        distinct = set(nums)
        if len(distinct) < 3:
            return max(distinct)
        else:
            for i in range(2):
                distinct.remove(max(distinct))
            return max(distinct)
        
sol = Solution() 
nums = [1,2,2,5,3,5]
res = sol.thirdMax(nums)
print(res)