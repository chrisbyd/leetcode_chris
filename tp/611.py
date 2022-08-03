from typing import List


## brutal force TLE
class Solution:
    ans = 0
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        ans = 0
        def dfs(index, res):

            if len(res) == 3 and res[0] + res[1] > res[2]:
                self.ans += 1
                return
            else:
                for i in range(index, len(nums)):
                    dfs(i+1, res + [nums[i]])
        
        dfs(0, [])
        
        return self.ans

## I am correct
## brutal force TLE
# ####o(n^3)
# class Solution:
#     ans = 0
#     def triangleNumber(self, nums: List[int]) -> int:
#         nums.sort()
#         ans = 0
#         length = len(nums)
#         for i in range(length):
#             for j in range(i+1, length):
#                 for k in range(j+1, length):
#                     if nums[i] + nums[j] <= nums[k]:
#                         break
#                     else:
#                         ans += 1
#         return ans

##o(n^2)

class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        ans = 0
        length = len(nums)
        for i in range(length-2):
            k = i + 2
            if nums[i] == 0:
                continue
            for j in range(i+1, length-1):
            
                while k < length and nums[i] + nums[j] > nums[k]:
                    k += 1
                ans += k - j - 1
        return ans
                
    
        
        
                
    
        
        
        
            