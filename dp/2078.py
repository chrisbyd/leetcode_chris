from typing import List

# naive brutal force solution
class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        ans = 0
        for i in range(len(colors)):
            for j in range(i+1, len(colors)):
                if colors[j] != colors[i] and j - i > ans:
                    ans = j - i
        return ans

sol  = Solution()
colors = [1,1,1,6,1,1,1]
colors = [1,8,3,8,3]
res = sol.maxDistance(colors)
print(res)
                    
# a two pointer solution  

class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        clr1 = colors[0]
        clr2 = colors[-1]
        ans = 0
        for i in range(1, len(colors)):
            if colors[i] != clr1 and i > ans:
                ans = i
        for j in range(len(colors) -1):
            if colors[j] != clr2 and len(colors) - j -1 > ans:
                ans = len(colors) - j -1
        return ans

sol  = Solution()
colors = [1,1,1,6,1,1,1]
#colors = [1,8,3,8,3]
res = sol.maxDistance(colors)
print(res)
               
        

