from typing import List


# the answer is wrong. The first should be smaller than the second one
class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        
        """
        nums.sort()
        n = len(nums)
        middle =  n//2 if n % 2 == 0 else n // 2 +1
      
        new_nums = [0 for _ in range(len(nums))]
        left, right = nums[:middle], nums[middle:]
        if n %2 == 0:
            i, j = 1, 0
        else: 
            i,j = 0, 1 
            
        for idx, num in enumerate(left):
            new_nums[i] = left[idx]
            i += 2

        for idx, num in enumerate(right):
            new_nums[j] = num
            j += 2
        
        for idx, num in enumerate(nums):
            nums[idx] = new_nums[idx]

sol = Solution()
input = [1,5,1,1,6,4]
sol.wiggleSort(input)
print(input)

class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        
        """
        nums.sort()
        n = len(nums)
        middle =  n//2 if n % 2 == 0 else n // 2 +1
        new_nums = [0 for _ in range(len(nums))]
        left, right = nums[:middle], nums[middle:]
        i = 1
        for num in reversed(right):
            new_nums[i] = num
            i += 2
        i = 0
        for num in reversed(left):
            new_nums[i] = num
            i += 2
        for idx, num  in enumerate(nums):
            nums[idx] = new_nums[idx]
        


sol = Solution()
input = [1,5,1,1,6,4]
sol.wiggleSort(input)
print(input)

