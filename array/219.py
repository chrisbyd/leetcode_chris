from typing import List

#Time limit exceeded
# class Solution:
#     def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
#         if len(nums) <= k:
#             if len(nums) == 1:
#                 return False
#             elif len(nums) != len(set(nums)):
#                 return True
#             return False
#         for i in range(len(nums)- k):
#             new_nums = nums[i:i+k+1]
#             if len(set(new_nums)) != len(new_nums):
#                 return True
#         return False


# sol = Solution()
# nums = [99,99]
# k = 2
# res =  sol.containsNearbyDuplicate(nums, k)
# print(res)


class Solution1:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hmap = {}
        for index, num in enumerate(nums):
            if num not in hmap:
                hmap[num] = index
            else:
                i = hmap[num]
                if index - i <= k:
                    return True
                else:
                    hmap[num] = index 
        return False

sol = Solution1()
nums = [1,0,1,1]
k = 1
res =  sol.containsNearbyDuplicate(nums, k)
print(res)