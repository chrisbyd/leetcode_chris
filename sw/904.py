from typing import List
from collections import defaultdict
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        unique = 0
        start = 0
        ans = 0
        hmap = defaultdict(int)
        for r in range(len(fruits)):
            if hmap[fruits[r]] == 0:
                unique += 1
            hmap[fruits[r]] += 1
            while unique > 2:
                if hmap[fruits[start]] == 1:
                    unique -=1
                hmap[fruits[start]] -= 1
                start += 1
            if unique <= 2:
                ans = max(ans, r - start + 1)
        return ans
                
                
            
                
            
sol = Solution()
fruits = [0,1,2,2]
res = sol.totalFruit(fruits)
print(res)