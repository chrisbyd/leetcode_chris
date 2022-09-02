from typing import List
### TLE
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        #@lru_cache(None)
        def dfs(index, subsets):
            if index == n:
                return True
            for i, sub in enumerate(subsets):
                if subsets[i] >= nums[index]:
                    subsets[i] -= nums[index]
                    if dfs(index+1 , subsets):
                        return True
                    subsets[i] += nums[index]
            return False
        target = sum(nums) 
        if target % k != 0:
            return False
        
        return dfs(0, [target // k] * k)

sol = Solution()

nums = [4,4,4,6,1,2,2,9,4,6]
k = 3
res = sol.canPartitionKSubsets(nums, k)
print(res)

from typing import List
### still tle
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        if sum(nums) % k != 0 :
            return False
        target = sum(nums) // k
        if max(nums) > target:
            return False
        @lru_cache(None)
        def dfs(mask, remain):
            if mask  ==  (1 << n) - 1:
                return 0
            ans = float('inf')
            for i in range(n):
                if (mask >>i) & 1 == 0:
                    if remain >= nums[i]:
                        ans = min(ans, dfs(mask | (1 << i), remain - nums[i]))
                    else:
                        ans = min(ans, 1 + dfs(mask | (1 << i), target - nums[i]))
            return ans
        return dfs(0, 0) == k
  

from typing import List
### still tle
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        if sum(nums) % k != 0 :
            return False
        target = sum(nums) // k
        if max(nums) > target:
            return False
        memo = {}
        def dfs(mask, remain):
            if (mask, remain) in memo:
                return memo[mask, remain]
            if mask  ==  (1 << n) - 1:
                return 0
            ans = float('inf')
            for i in range(n):
                if (mask >>i) & 1 == 0:
                    if remain >= nums[i]:
                        ans = min(ans, dfs(mask | (1 << i), remain - nums[i]))
                    else:
                        ans = min(ans, 1 + dfs(mask | (1 << i), target - nums[i]))
            memo[mask, remain] = ans
            return ans
        return dfs(0, 0) == k
# sol = Solution()
# nums = [3522,181,521,515,304,123,2512,312,922,407,146,1932,4037,2646,3871,269]
# k = 5
# res = sol.canPartitionKSubsets(nums, k)
# print(res)

### to further minimize the time
from typing import List
###
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        if sum(nums) % k != 0 :
            return False
        target = sum(nums) // k
        if max(nums) > target:
            return False
        memo = {}
        def dfs(mask):
            if mask in memo:
                return memo[mask]
            if mask == (1 << n) -1:
                return 0, 0
            ans = float('inf')
            remain = 0
            for i in range(n):
                if (mask >> i) & 1 == 0:
                    ans1, remain1 = dfs(mask | (1 << i))
                    if remain1 >= nums[i]:
                        remain1 = remain1 - nums[i]
                    else:
                        ans1 = 1 + ans1
                        remain1 = target - nums[i]
                    if ans1 < ans or (ans1 == ans and remain1 > remain):
                        ans = ans1
                        remain = remain1
            memo[mask] = (ans, remain)
            return ans, remain
        return dfs(0)[0] == k 
                    
sol = Solution()
nums = [3522,181,521,515,304,123,2512,312,922,407,146,1932,4037,2646,3871,269]
k = 5
# nums = [4,3,2,3,5,2,1]
# k = 4
nums = [7628,3147,7137,2578,7742,2746,4264,7704,9532,9679,8963,3223,2133,7792,5911,3979]
k = 6
num = [3,9,4,5,8,8,7,9,3,6,2,10,10,4,10,2]
k = 10

res = sol.canPartitionKSubsets(nums, k)
print(res)