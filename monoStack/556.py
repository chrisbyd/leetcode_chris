from collections import deque

class Solution:
    def nextGreaterElement(self, n: int) -> int:
        nums= [int(num) for num in list(str(n))]
        length = len(nums)
        start = length - 1
        while start >= 1:
            if nums[start-1] < nums[start]:
                break
            start -= 1
        if start == 0:
            return -1
        larger_index = length - 1
        for i in range(length-1, start-1, -1):
            if nums[i] > nums[start -1]:
                larger_index = i
                break
        
        nums[start-1], nums[larger_index] = nums[larger_index], nums[start - 1]
        nums = nums[:start] + sorted(nums[start:])
        ans = 0
        for num in nums:
            ans = ans * 10 + num
        max_val = 2 ** 31 - 1
        return ans if ans <= max_val else -1
            
        

            
            
            
        
sol = Solution()
n = 1342
res = sol.nextGreaterElement(n)
print(res)