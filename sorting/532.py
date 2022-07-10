from typing import List

### complexity o(n^2)
#### time limit exceeded
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        occur = {}
        n = len(nums)
        ans = 0
        for i in range(n):
            for j in range(i + 1, n):
                if abs(nums[i] - nums[j]) == k and (nums[i], nums[j]) not in occur:
                
                    ans += 1
                    occur[nums[i], nums[j]] = 1
                    occur[nums[j], nums[i]] = 1
        return ans
    
sol =  Solution()
nums = [1,3,1,5,4]
k = 0
res = sol.findPairs(nums, k)
print(res)

### with dynamic programming
from collections import defaultdict
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [0 for i in range(n)]
        nums.sort()
        num_set = set([nums[0]])
  
        for i in range(1, n):
            if nums[i] not in num_set:
                if nums[i] - k in num_set:
                    dp[i] = dp[i-1] + 1
                else:
                    dp[i] = dp[i-1]
            else:
                dp[i] = dp[i-1]
            num_set.add(nums[i])

        dic_freq = defaultdict(int)
        for num in nums:
            dic_freq[num] += 1

        ans_k_0 = 0
        for key in dic_freq.keys():
            if dic_freq[key] > 1:
                ans_k_0 += 1
                
        return dp[-1] if k != 0 else ans_k_0
                    
                
            

    
sol =  Solution()
nums = [1,2,4,4,3,3,0,9,2,3]
k = 3
res = sol.findPairs(nums, k)
print(res)
 