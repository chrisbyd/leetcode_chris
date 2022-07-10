from typing import List

# not accepted for extreme cases where  a million recurions are needed
class Solution:
    def minMoves(self, nums: List[int]) -> int:
        ans = 0
        def dfs(nums, ans):
            print(nums)
            if len(set(nums)) == 1:
                return ans

            else:
                max_value = max(nums)
                count = 1
                for idx, num in enumerate(nums):
                    if num == max_value and count == 1:
                        count -= 1
                    else:
                        nums[idx] += 1
                return dfs(nums, ans + 1)
        return dfs(nums, 0)

sol = Solution()

nums = [1,1,1]  
res = sol.minMoves(nums)
print(res)                


# with bottom up not with recursion
# Still TLE   Not accepted
class Solution1:
    def minMoves(self, nums: List[int]) -> int:
        ans = 0
        while len(set(nums)) != 1:
            ans += 1
            max_value = max(nums)
            count = 1
            for idx, num in enumerate(nums):
                    if num == max_value and count == 1:
                        count -= 1
                    else:
                        nums[idx] += 1
        return ans

sol = Solution1() 
nums = [1,2,3]  
res = sol.minMoves(nums)
print(res)    

# what the fuck??? WtF   
class Solution(object):
    def minMoves(self, a):
        return sum(a)-len(a)*min(a)

# Another solution by leetcode
class Solution3:
    def minMoves(self, nums):
        min_value = min(nums)
        ans = 0
        for num in nums:
            ans += num - min_value
        return ans

sol = Solution()
nums = [1,2,3]  
res = sol.minMoves(nums)
print(res)

