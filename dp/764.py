from typing import List
from collections import defaultdict

# ## TLe error
# class Solution:
#     def orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:
#         mineDict = {}
#         for x, y in mines:
#             mineDict[x, y] = 0
#         dp = defaultdict(list)
#         length = n // 2 + 1
#         for x in range(n):
#             for y in range(n):
#                 if (x,y) not in mineDict:
#                     dp[0].append((x,y))
#         directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
#         for i in range(1, length):
#             if len(dp[i-1]) == 0:
#                 return i-1 

#             for x, y in dp[i-1]:
#                 valid = True
#                 for xx, yy in directions:
#                     new_x = x + i * xx
#                     new_y = y + i * yy
#                     if not (new_x >= 0 and new_x <= n - 1 and new_y >= 0 and new_y <= n -1 and (new_x, new_y) not in mineDict):
#                         valid = False
#                 if valid:
#                     dp[i].append((x,y))
      
#         return length if dp[length -1] else length - 1




# sol = Solution()
# n = 2
# mines = [[0,0],[0,1],[1,0],[1,1]]
# res = sol.orderOfLargestPlusSign(n, mines)
# print(res)


# a new dynamic programming solution

class Solution:
    def orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:
        dp = [[0 for j in range(n+2)] for i in range(n+2)]
        banned = set()
        for mine in mines:
            banned.add((mine[0], mine[1])) 

        for x in range(1,n+1):
            count = 0
            for y in range(1,n+1):
                count = 0 if (x-1,y-1) in banned else count +1
                dp[x][y] = count
            
            count = 0
            for y in range(n, 0, -1):
                count = 0 if (x-1,y-1) in banned else count + 1
                dp[x][y] = min(dp[x][y], count)

        for y in range(1,n+1):
            count = 0
            for x in range(1, n+1):
                count = 0 if (x-1,y-1) in banned else count + 1
                dp[x][y] =  min(dp[x][y], count)
            
            count = 0
            for x in range(n, 0, -1):
                count = 0 if (x-1,y-1) in banned else count + 1
                dp[x][y] = min(dp[x][y], count)
        ans = 0 
     
        for line in dp:
            ans = max(ans, max(line))
        return ans
    

n = 3
mines = [[0,1]]
sol = Solution()
res = sol.orderOfLargestPlusSign(n, mines)
print(res)







        
        