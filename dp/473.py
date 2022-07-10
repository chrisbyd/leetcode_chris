from typing import List

# dynamic programming
class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        m = len(matchsticks)
        
        if m < 4: return False
        elif sum(matchsticks) % 4 != 0:
            return False
        side_length = sum(matchsticks) // 4
        memo = {}
        def recursive(mask, sides_done):
            total = 0
            for i in range(m - 1, -1, -1):
                if not (mask & (1 << i)):
                    total += matchsticks[m - 1 - i]

            if total > 0 and  total % side_length == 0:
                sides_done = total // side_length
            if sides_done == 3:
                return True
            if (mask, sides_done) in memo:
                return memo[(mask, sides_done)]
            
            ans = False
            residual = side_length - total % side_length
            for i in range(m-1, -1, -1):
                if matchsticks[m -1-i] <= residual and mask & (1<<i):
                    if recursive(mask ^ (1 << i), sides_done):
                        ans = True
                        break
            memo[(mask, sides_done)] = ans
            return ans 
        return  recursive((1<<m) -1, 0)

#
       
class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        m = len(matchsticks)
        if m < 4: return False
        elif sum(matchsticks) % 4 != 0: return False
        side_length = sum(matchsticks) // 4
        memo = {}
        def recursive(mask, sides_done):
            if sides_done == 3:
                return True
            total = 0
            for i in range(m - 1, -1, -1):
                if not (mask & (1 << i)):
                    total += matchsticks[m - 1 - i]
            res = side_length - total % side_length 
           
            if (mask, sides_done) not in memo:
                for i in range(m-1, -1, -1):
                    if matchsticks[m-1-i] <= res and mask & (1 << i):
                        if matchsticks[m-1 -i] == res:
                            if recursive(mask ^(1<<i), sides_done + 1):
                                memo[(mask, sides_done)] = True
                                return True
                        else:
                            if recursive(mask ^(1<<i), sides_done):
                                memo[(mask, sides_done)] = True
                                return True 
                memo[(mask, sides_done)] = False
                return False
    
            else:
                return memo[(mask, sides_done)]
        return recursive((1 << m) - 1, 0)

sol = Solution()
matchsticks = [1,1,2,2,3]
res = sol.makesquare(matchsticks)
print(res)





        
        
        
        