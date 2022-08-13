
class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        def dp(arr, val):
            if arr[-1] >= val:
                return True
            for i, num in enumerate(arr):
                print(i, num, val)
                new_array = arr[:i] + arr[i+1:]
                if not dp(new_array, val - num):
                    return True
            return False
        if desiredTotal == 0 or desiredTotal <= maxChoosableInteger:
            return True
        if (maxChoosableInteger + 1) / 2 * maxChoosableInteger < desiredTotal:
            return False
        return dp([i for i in range(1,maxChoosableInteger + 1)], desiredTotal)
                    
                
sol = Solution()
m = 4
d = 6
res = sol.canIWin(m, d)
print(res)

###not elegent althogh it passed

class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        @lru_cache(None)
        def dp(arr, val):
            arr = list(arr)
            if arr[-1] >= val:
                return True
            for i, num in enumerate(arr):
                new_array = arr[:i] + arr[i+1:]
                if not dp(tuple(new_array), val - num):
                    return True
            return False
        if desiredTotal == 0 or desiredTotal <= maxChoosableInteger:
            return True
        if (maxChoosableInteger + 1) / 2 * maxChoosableInteger < desiredTotal:
            return False
        return dp(tuple([i for i in range(1,maxChoosableInteger + 1)]), desiredTotal)
                    