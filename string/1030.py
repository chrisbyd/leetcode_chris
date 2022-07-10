
# simple solution with hashmap
from typing import List
import collections
class Solution:
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> List[List[int]]:
        hmap = collections.defaultdict(list)
        for i in range(rows):
            for j in range(cols):
                d = abs(i - rCenter) + abs(j - cCenter)
                hmap[d].append([i,j])
        longest = rows + cols
        ans = []
        for i in range(longest + 1):
            if i in hmap:
                ans.extend(hmap[i])
        return ans

sol = Solution()
rows = 2
cols = 2
rCenter = 0
cCenter = 1
res = sol.allCellsDistOrder(rows, cols, rCenter, cCenter)
print(res)

        

        