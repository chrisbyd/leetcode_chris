from typing import List
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        new_nums = []
        start = len(nums) - 1
        for i in range(len(nums)):
            if nums[i] >=0:
                start = i
                break
        left, right = start -1, start
        while left >= 0 :
            if right < len(nums) and abs(nums[left])  > abs(nums[right]):
                new_nums.append(nums[right] ** 2)
                right += 1
            else:
                new_nums.append(nums[left]**2)
                left -= 1
        while right < len(nums):
            new_nums.append(nums[right] **2)
            right += 1
        return new_nums