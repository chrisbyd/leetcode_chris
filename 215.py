from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        return nums[-k]

sol = Solution()
nums = [3,2,1,5,6,4] 
k = 3
res = sol.findKthLargest(nums,k)
print(res)