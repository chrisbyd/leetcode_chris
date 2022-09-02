from typing import List
from typing import List

class Solution:
    ans = float('inf')
    def minAbsDifference(self, nums: List[int], goal: int) -> int:
        n = len(nums)
 
        def dfs(index, cursum):
            if index == n:
                self.ans = min(self.ans, abs(goal - cursum))
                return 
            dfs(index + 1, cursum + nums[index])
            dfs(index + 1, cursum)
        dfs(0, 0)
        return self.ans

sol = Solution()
nums = [7,-9,15,-2]
goal = -5
res = sol.minAbsDifference(nums, goal)
print(res)
               
            


       
            
        