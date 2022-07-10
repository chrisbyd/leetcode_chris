from typing import List

#### Time Limit exceeded
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        ans = []
        def backtrack(nums, residual, cur):
            if residual < 0:
                return
            elif residual == 0:
                ans.append(cur[:])
            else:
                for num in nums:
                    cur.append(num)
                    backtrack(nums, residual- num, cur)
                    cur.remove(num)
        backtrack(nums, target, [])
        return len(ans)

# sol = Solution()
# nums = [4,2,1]
# target = 32
# # result = 39882198
# res = sol.combinationSum4(nums, target)
# print(res)


# Consider solving with dynamic programming
# This is a bottom up dynamic programming solution
#lets consider solving it with top-down dynamic programming

class Solution1:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        nums.sort()
        dp = [0 for _ in range(target+1)]
        for i in range(1,target + 1):
            cumu = 0
            for j in range(len(nums)):
                if i - nums[j] > 0:
                    cumu += dp[i - nums[j]]
                elif i - nums[j] == 0:
                    cumu += 1
               
            dp[i] = cumu
       
        return dp[target]

sol = Solution1()
nums = [4,2,1]
target = 32
res = sol.combinationSum4(nums, target)
print(res)

# top down dynamic programming
class Solution2:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        mem = [-1 for _ in range(target + 1)]
        def dp(residual):
            if residual <= 0:
                return 0
            elif mem[residual] != -1:
                return mem[residual]
            else:
                cumu = 0
                for num in nums:
                    if residual - num == 0:
                        cumu += 1
                    else:
                        cumu += dp(residual - num)
                mem[residual] = cumu 
            return mem[residual]
        return dp(target)
sol = Solution2()
nums = [4,2,1]
target = 32
res = sol.combinationSum4(nums, target)
print(res)        

# top down dynamic programming,, optimized code
class Solution3:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        mem = [-1 for _ in range(target + 1)]
        mem[0] = 1
        def dp(residual):
            if residual < 0:
                return 0
            elif mem[residual] != -1:
                return mem[residual]
            else:
                cumu = 0
                for num in nums:
                    cumu += dp(residual - num)
                mem[residual] = cumu 
            return mem[residual]
        return dp(target)
            

sol = Solution3()
nums = [4,2,1]
target = 32
res = sol.combinationSum4(nums, target)
print(res)        

      

        
        