from typing import List
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)
        left, right = 0, len(nums) -1
        while left <= right:
            if nums[left] == sorted_nums[left]:
                left += 1
            elif nums[right] == sorted_nums[right]:
                right -= 1
            else:
                break
        return right - left + 1
        