from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        n = len(nums)
        new_nums = nums[-k:] + nums[:n-k]
        for i,_ in enumerate(nums):
            nums[i] = new_nums[i]
       
    
nums = [1,2,3,4,5,6,7]
k = 3

sol = Solution() 
sol.rotate(nums,k)
print(nums)