from itertools import count
from typing import List
import collections





import math
class Solution1:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        ans = 0
        for i in range(len(points)):
            hmap = collections.defaultdict(int)
            for j in range(len(points)):
                distance = math.pow((points[i][0] - points[j][0]),2) + math.pow((points[i][1] - points[j][1]),2)
                hmap[distance] += 1
            for count in hmap.values():
                if count >=2:
                    ans += count * (count -1)
        return ans




points = [[0,0],[1,0],[-1,0],[0,1],[0,-1]]
points = [[0,0],[1,0],[2,0]]
sol = Solution1()
res= sol.numberOfBoomerangs(points)
print(res)

                 



        