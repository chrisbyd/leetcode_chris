from typing import List

class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        nnums = sorted(nums)
        half = n - n // 2
        cur = half - 1
        start = 0
        while cur >= 0:
            nums[start] = nnums[cur]
            start += 2
            cur -= 1
        start = 1
        cur = n-1
        length = n -half
        while length > 0:
            nums[start] = nnums[cur]
            cur -= 1
            start += 2
            length -= 1
        return nums
            
            
sol = Solution()
nums = [1,5,1,1,6,4]
res = sol.wiggleSort(nums)
print(res)
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
            nums[idx] = new_nums[