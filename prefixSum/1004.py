from typing import List
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        stack, zeros, ans = [], 0, 0
        for num in nums:
            stack.append(num)
            if num == 0:
                zeros += 1
            if zeros <=k:
                ans = max(ans, len(stack))
            while zeros > k:
                num1 = stack.pop(0)
                if  num1 == 0:
                    zeros -= 1
        return ans
            
        
        
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        count, ans, j = 0, 0, 0
        for i in range(len(nums)):
            if nums[i] == 0:
                count += 1
            if count <= k:
                ans = max(ans, i- j+ 1)
            while count > k:
                if nums[j] == 0:
                    count -=1
                j += 1
           
        return max(ans, i - j + 1)
nums = [1,1,1,0,0,0,1,1,1,1,0]
k = 2
sol = Solution()
res = sol.longestOnes(nums, k)
print(res)