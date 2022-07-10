# a simple recursion without memorization

# its correct but exceeds the time limit
# try to add memorization

from functools import lru_cache
from tkinter.messagebox import NO
class Solution: 
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        if maxChoosableInteger * (1 +maxChoosableInteger) / 2 < desiredTotal:
            return False
        usedInteger = set()
        @lru_cache(None)
        def dp(player, runningScore):
            if player == 0:
                ans = False
            else:
                ans = True
            for i in range(1, maxChoosableInteger +1):
                if player == 0:
                    if i not in usedInteger:
                        if runningScore + i >= desiredTotal:
                            return True
                        else:
                            usedInteger.add(i) 
                            ans = ans or dp(1 - player, runningScore + i)
                            usedInteger.remove(i)
                else:
                    if i not in usedInteger:
                        if runningScore + i >= desiredTotal:

                            return False
                        else:
                            usedInteger.add(i)
                            ans = ans and dp(1 - player, runningScore + i)
                            usedInteger.remove(i)
            return ans
        return dp(0, 0)
            
                
sol = Solution()
maxChoosableInteger = 5
desiredTotal = 12
res = sol.canIWin(maxChoosableInteger, desiredTotal)
print(res)




from functools import lru_cache
class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        if maxChoosableInteger * (1 +maxChoosableInteger) / 2 < desiredTotal:
            return False
        usedInteger = set()
        def dp(player, runningScore):
            for i in range(1, maxChoosableInteger +1):
                if player == 0:
                    ans = False
                    if i not in usedInteger:
                        if runningScore + i >= desiredTotal:
                            return True
                        else:
                            usedInteger.add(i)
                            ans = ans or dp(1 - player, runningScore + i)
                            usedInteger.remove(i)
                            if ans:
                                return True
                else:
                    ans = True
                    if i not in usedInteger:
                        if runningScore + i >= desiredTotal:

                            return False
                        else:
                            usedInteger.add(i)
                            ans = ans and dp(1 - player, runningScore + i)
                            usedInteger.remove(i)
                            if not ans:
                                return False
            return ans
        return dp(0, 0)



                
sol = Solution()
maxChoosableInteger = 5
desiredTotal =12
res = sol.canIWin(maxChoosableInteger, desiredTotal)
print(res)


class Solution:
    def canIWin(self, Max: int, total: int) -> bool:
        @lru_cache(None)
        def dp(arr, value):
            if arr[-1] >= value: return True
            for i in range(len(arr)):
                new_arr = arr[:i] + arr[i+1:]
                if not dp(new_arr, value - arr[i]):
                    return True
            return False




















































































































