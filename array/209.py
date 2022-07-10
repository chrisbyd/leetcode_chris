from typing import List

# class Solution:
#     def minSubArrayLen(self, target: int, nums: List[int]) -> int:
#         def dp(nums):
#             if len(nums) == 1:
#                 return 0 if nums[0] < target else 1
#             elif sum(nums) < target:
#                 return 0
#             elif sum(nums) == target:
#                 return len(nums)
#             else:
#                 res = [len(nums)]
           
#                 out1 = dp(nums[1:])
#                 out2 = dp(nums[:-1])
#                 if out1 != 0:
#                     res.append(out1)
#                 if out2 != 0:
#                     res.append(out2)
#                 return min(res)
#         return dp(nums)


# sol = Solution()

# target = 20
# nums = [1,2,3,4,10]
# res = sol.minSubArrayLen(target, nums)
# print(res)

# resolve the problem with iterative technique

#This solution :::: memory limit exceeded  Too much memory for storing the result
# class Solution1:
#     def minSubArrayLen(self, target: int, nums: List[int]) -> int:
#         self.result = [[-1 for j in range(0, len(nums) -i +1 ) ] for i in range(len(nums)+1)]
       
#         for i in range(1, len(nums)+1):
#             for j in range(0, len(nums) - i +1):
#                 if  i > 1:
#                    # print("i:{},j:{}".format(i,j))
#                     res = self.result[i-1][j] + nums[j+i-1]
#                     self.result[i][j] = res
#                 else:
#                     res = nums[j]
#                   #  print("i:{},j:{}".format(i,j))
#                     self.result[i][j] = res
                    
#                 if res >= target:
#                     return i
#         return 0



class Solution1:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        self.sum = nums[:]
        for index, num in enumerate(nums):
            if index == 0:
                self.sum[index] = num
            else:
                self.sum[index] = self.sum[index - 1] + self.sum[index]
    
        for i in range(len(nums)):
            for j in range(0, len(nums)-i):
                res = self.sum[j+i] - self.sum[j] + nums[j]
              
                if res >= target:
                    return i+1
        return 0

sol = Solution1()

target = 11
nums =  [1,1,1,1,1,1,1,1]
res = sol.minSubArrayLen(target, nums)
print(res)

# #Binary search solution

# class Solution:
#     def minSubArrayLen(self, target: int, nums: List[int]) -> int:




        
