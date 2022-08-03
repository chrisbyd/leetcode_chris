# this problem is easy but be sure to take care of the max operation
# class Solution:
#     def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
#         i, j = 0,  k
#         ans = []
#         if k>= len(nums):
#             return [max(nums)]
#         while j <= len(nums):
#             ans. append(max(nums[i:j]))
#             i += 1
#             j+= 1
#         return ans


from heapq import heappush, heappop
from typing import List
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans, heap = [], []
        for i in range(k-1):
            heappush(heap, (-nums[i], i))
  
        for i in range(k-1, len(nums)):
            heappush(heap, (-nums[i], i))
     
            while heap[0][1] < i - k + 1:
                heappop(heap)
            val, index = heap[0]
            ans.append(-val)
        return ans
                
sol = Solution()
nums = [1,3,-1,-3,5,3,6,7]
k = 3
res = sol.maxSlidingWindow(nums, k)
print(res)
        