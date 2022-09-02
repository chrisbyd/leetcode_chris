from typing import List

### tle
class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        tsum  = sum(matchsticks)
        if tsum % 4 != 0:
            return False
        target = tsum // 4
        if max(matchsticks) > target:
            return False
        n = len(matchsticks)
        def dfs(index, subsets):
            if index == n:
                return True
            for i, sub in enumerate(subsets):
                if sub >= matchsticks[index]:
                    subsets[i] -= matchsticks[index]
                    if dfs(index+1, subsets):
                        return True
                    subsets[i] += matchsticks[index]
                    if not subsets[i]:
                        break 
            return False
        return dfs(0, [target] * 4)
###tle
from typing import List
class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        tsum  = sum(matchsticks)
        if tsum % 4 != 0:
            return False
        target = tsum // 4
        if max(matchsticks) > target:
            return False
        n = len(matchsticks)
        def dfs(mask):
            if mask == (1 << n) - 1:
                return 0, 0
            ans = float('inf')
            remain = 0
            for i in range(n):
                if (mask >> i) & 1 == 0:
                    ans1, remain1 = dfs(mask | (1 << i))
                    if remain1 >=  matchsticks[i]:
                        remain1 -= matchsticks[i]
                    else:
                        ans1 += 1
                        remain1 = target - matchsticks[i]
                    if ans1 < ans or (ans1 == ans and remain1 > remain):
                        ans = ans1
                        remain = remain1
            return ans, remain
        return dfs(0)[0] == 4
sol = Solution()
nums = [1,1,2,2,2]
res = sol.makesquare(nums)
print(res)

###dynamic programming
class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        tsum  = sum(matchsticks)
        if tsum % 4 != 0:
            return False
        target = tsum // 4
        if max(matchsticks) > target:
            return False
        n = len(matchsticks)
        @cache
        def dfs(mask):
            if mask == (1 << n) - 1:
                return 0
            for i in range(n):
                if (mask >> i) & 1 == 0:
                    neighbor = dfs(mask | (1 << i))
                    if neighbor >= 0 and neighbor + matchsticks[i] <= target:
                        return (neighbor + matchsticks[i]) % target
            return -1
        return dfs(0) == 0

### solution 2
class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        tsum  = sum(matchsticks)
        if tsum % 4 != 0:
            return False
        target = tsum // 4
        if max(matchsticks) > target:
            return False
        print(target)
        n = len(matchsticks)
      #  @cache
        def dfs(mask):
            if mask == (1 << n) - 1:
                return target
            for i in range(n):
                if (mask >> i) & 1 == 0:
                    remain = dfs(mask | (1 << i))
                    if remain >= 0 and matchsticks[i] <= remain:
                        if matchsticks[i] == remain:
                            remain = target
                        elif matchsticks[i] < remain:
                            remain -= matchsticks[i]
                        return remain
            return -1
        return dfs(0) == target 

sol = Solution()
nums = [5,5,5,5,4,4,4,4,3,3,3,3]
res = sol.makesquare(nums)
print(res)