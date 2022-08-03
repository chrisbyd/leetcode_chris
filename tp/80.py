from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i , j = 0, 0
        count = 1
        n = len(nums)
        if n == 1:
            return 1
        prev = nums[0]
        while j < n-1:
            j = j + 1
            if nums[j] == prev:
                count +=1
            elif nums[j] != prev:
                count = 1
                prev = nums[j]
            if count <= 2:
                i = i + 1
                nums[i] = nums[j]
        return i+1


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        length = len(nums)
        new_nums = [nums[0]]
        counter = 1
        for i in range(1, length):
            if nums[i] == nums[i-1]:
                counter += 1
            else:
                counter = 1
            if  counter < 3:
                new_nums.append(nums[i])
        for i in range(len(new_nums)):
            nums[i] = new_nums[i]
        return len(new_nums)
            