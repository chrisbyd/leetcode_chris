class Solution:
    def isIdealPermutation(self, nums: List[int]) -> bool:
        if nums[0] != 0 and nums[1] != 0:
            return False
        n = len(nums)
        for i in range(1, n):
            if nums[i] != i and nums[i-1] != i:
                return False
        return True
        
class Solution:
    def isIdealPermutation(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return True
        if nums[0] != 0 and nums[1] != 0:
            return False
        n = len(nums)
        for i in range(1, n-1):
            if nums[i] != i and nums[i-1] != i and nums[i+1] != i:
                return False
        if nums[n-1] != n-1 and nums[n-2] != n-1:
            return False
        return True
        
class Solution:
    def isIdealPermutation(self, nums: List[int]) -> bool:
        """A local inversion is a global inversion, 
        hence all inversions must be local. 
        That is, a number is at most 1 index away from its sorted index
		"""
        
        for i, num in enumerate(nums):
            if abs(num - i) > 1:
                return False 
            
        return True