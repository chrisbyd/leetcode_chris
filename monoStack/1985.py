# import random
# ##TLE quick select
# class Solution:
#     def kthLargestNumber(self, nums: List[str], k: int) -> str:
#         nums = [int(num) for num in nums]
#         def quicksort(nums, k ):
#             # if len(nums) == 1:
#             #     return nums[0]
#             rindex = random.randint(0, len(nums)-1)
#             pivot = nums[rindex]
#             left, right = [], []
#             for i, num in enumerate(nums):
#                 if i == rindex: 
#                     continue
#                 if num <= pivot:
#                     left.append(num)
#                 else:
#                     right.append(num)
#             if len(right) == k-1:
#                 return pivot
#             if len(right) > k- 1:
#                 return quicksort(right, k)
#             else:
#                 return quicksort(left, k - len(right) -1)
#         res = quicksort(nums, k)
#         return str(res)


### edge case with o(n^2) complexity
from typing import List
import random
class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        n = len(nums)
        k = len(nums) - k + 1
        nums = [int(num) for num in nums]
        def quickselect(l, r,  k ):
            print(l ,r, k, nums)
            pivot, p = nums[r], l
            for i in range(l, r):
                if nums[i] <= pivot:
                    nums[i], nums[p] = nums[p], nums[i]
                    p += 1
            nums[p], nums[r] = nums[r], nums[p]
           
            if k-1 == p - l:
                return nums[p]
            elif k - 1 < p - l:
                return quickselect(l, p-1, k)
            else:
                return quickselect(p+1, r,  k - p + l -1)
        return str(quickselect(0, n-1, k))

sol = Solution()
nums = ["77","969","71","7405","87","61","950","5317","4"]


k = 1
res = sol.kthLargestNumber(nums, k)
print(res)

###you could solve it with heap