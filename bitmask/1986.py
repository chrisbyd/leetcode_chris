from typing import List
###bitmasking
class Solution:
    def minSessions(self, tasks: List[int], sessionTime: int) -> int:
        n = len(tasks)
        def backtrack(index, sessions):
            if index == n:
                return True
            for i, session in enumerate(sessions):
                if session >= tasks[index]:
                    sessions[i] -= tasks[index]
                    if backtrack(index + 1, sessions):
                        return True
                    sessions[i] += tasks[index]
                    if sessions[i] == sessionTime:
                        break
            return False
        l, r = 1, len(tasks)
        while l <= r:
            mid = (l + r) // 2
            sts = [sessionTime] * mid
            if backtrack(0, sts):
                r = mid - 1
            else:
                l = mid +1
        return l


from typing import List
###bitmasking
class Solution:
    def minSessions(self, tasks: List[int], sessionTime: int) -> int:
        n = len(tasks) 
      #  @lru_cache(None)
        def dp(mask, remainTime):
            if mask == (1 << n) - 1:
                print((1 << n) - 1)
                return 0
            ans = float('inf')
            for i in range(n):
                if (mask >> i ) & 1 == 0:
                    if remainTime >= tasks[i]:
                        ans = min(ans, dp(mask | 1 << i, remainTime - tasks[i]))
                    else:
                        ans = min(ans, 1 + dp(mask | 1 << i, sessionTime - tasks[i]))
            return ans
        return dp(0, 0)

sol = Solution()

tasks = [1,2,3]
st = 3
res = sol.minSessions(tasks, st)
print(res)         


from typing import List
###bitmasking
class Solution:
    def minSessions(self, tasks: List[int], sessionTime: int) -> int:
        n = len(tasks) 
      #  @lru_cache(None)
        def dp(mask, remainTime):
            if mask == (1 << n) - 1:
                 
                return 0
            ans = float('inf')
            for i in range(n):
                if (mask >> i ) & 1 == 0:
                    if remainTime >= tasks[i]:
                        ans = min(ans, dp(mask | 1 << i, remainTime - tasks[i]))
                    else:
                        ans = min(ans, 1 + dp(mask | 1 << i, sessionTime - tasks[i]))
            return ans
        return dp(0, 0)


### to further minimize the time
class Solution:
    def minSessions(self, tasks: List[int], sessionTime: int) -> int:
        n = len(tasks) 
      #  @lru_cache(None)
        def dp(mask, remainTime):
            if mask == (1 << n) - 1:
                 
                return 0
            ans = float('inf')
            for i in range(n):
                if (mask >> i ) & 1 == 0:
                    if remainTime >= tasks[i]:
                        ans = min(ans, dp(mask | 1 << i, remainTime - tasks[i]))
                    else:
                        ans = min(ans, 1 + dp(mask | 1 << i, sessionTime - tasks[i]))
            return ans
        return dp(0, 0)




from typing import List
###bitmasking
class Solution:
    def minSessions(self, tasks: List[int], sessionTime: int) -> int:
        n = len(tasks) 
        @lru_cache(None)
        def dp(mask):
            if mask == (1 << n) - 1:
                return 0, 0
            ans = float('inf')
            remainTime = 0
            for i in range(n):
                if (mask >> i) & 1 == 0:
                    ans1, remainTime1 = dp(mask |  (1 << i))
                    if remainTime >= tasks[i]:
                        remainTime1 -= tasks[i]
                    else:
                        ans1 += 1
                        remainTime1 = sessionTime - tasks[i]
                    if ans1 < ans or ( ans1 == ans and remainTime1 > remainTime):
                        ans = ans1
                        remainTime = remainTime1
            return ans, remainTime
                    
          
        return dp(0)[0]
                        

                        