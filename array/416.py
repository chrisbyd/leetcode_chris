from typing import List

# time limit exceeded
#But the ans is correct

class Solution:
    def canPartition(self, nums):
        t_sum = sum(nums)
        if t_sum % 2 !=0:
            return False
        h_sum = t_sum // 2
        def dfs(nums, c_sum):
            if c_sum == h_sum:
                return True
            elif len(nums) == 0:
                return False
            for i in range(len(nums)):
                if dfs(nums[i+1:], c_sum + nums[i]):
                    return True
            return False
        
        return dfs(nums, 0)

sol = Solution() 
nums = [1,2,5]
res = sol.canPartition(nums)
print(res)

# time limited exceeded
# 0 1 backpacking problem
class Solution1:
    def canPartition(self, nums):
        t_sum = sum(nums)
        if t_sum % 2 !=0:
            return False
        target = t_sum // 2
        def checkSubset(index, c_sum):
            if c_sum == target:
                return True
            elif index == len(nums):
                return False
            return checkSubset(index +1, c_sum) or checkSubset(index+1, c_sum + nums[index])
        return checkSubset(0, 0)
        
nums = [1,1,2,2]
sol = Solution1()
res = sol.canPartition(nums)
print(res)



import collections

class Solution2:
    def canPartition(self, nums):
        t_sum = sum(nums)
        if t_sum % 2 !=0:
            return False
        target = t_sum // 2
        dp = collections.defaultdict(int)
        def checkSubset(index, c_sum):
            if c_sum == target:
                return True
            elif index == len(nums):
                return False
            elif dp[index, c_sum] != 0:
                return True if dp[index, c_sum] ==1 else False
            if checkSubset(index +1, c_sum) or checkSubset(index+1, c_sum + nums[index]):
                dp[index, c_sum] = 1
                return True
            else:
                dp[index, c_sum] = 2
                return False 
        return checkSubset(0, 0)
        

        
nums = [1,1,2,2]
sol = Solution2()
res = sol.canPartition(nums)
print(res)
