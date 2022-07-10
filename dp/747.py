from typing import List

from django.template import Origin
class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        Origin_nums = nums[:]
        nums.sort()
        if len(nums) == 1:
            return 0
        largest = nums[-1]
        for num in reversed(nums[:-1]):
       
            if largest - num * 2 < 0:
                print("hello")
                return -1
        return Origin_nums.index(largest)

sol = Solution()
nums = [3,6,1,0]
res = sol.dominantIndex(nums)
print(res)