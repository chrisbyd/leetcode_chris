# class Solution:
#     def trap(self, height: List[int]) -> int:
#         n = len(height)
#         left, right = 0,  len(height) -1
#         left_max, right_max = height[0], height[-1]
#         ans = 0
#         rmax = []
#         cur_max = 0
#         for i in range(n-1, -1, -1):
#             rmax.append(cur_max)
#             cur_max = max(cur_max, height[i])
#         rmax = rmax[::-1]
#         for i in range(n):
#             water = min(left_max, rmax[i])  - height[i]
#             ans += max(0, water)
#             left_max = max(left_max, height[i])
#         return ans


### with two pointers
from typing import List
class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        ans = 0
        left_max, right_max = height[0], height[-1]
        while left <= right:
            if right_max < left_max:
                water = max(0,  right_max - height[right])
                right_max = max(right_max, height[right])
                print(right_max, height[right])
                print(left, right, water)
                right -= 1
                ans += water
            else:
                water = max(0, left_max - height[left])
                print(left, right, water)
                left_max = max(left_max, height[left])
                left +=1
                ans += water
        return ans

sol = Solution()
height = [0,1,0,2,1,0,1,3,2,1,2,1]
res = sol.trap(height)
print(res)
        