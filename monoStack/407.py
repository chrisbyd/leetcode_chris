from typing import List
from copy import deepcopy
from typing import List
class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        m, n = len(heightMap), len(heightMap[0])
        tmax, bmax, lmax, rmax = deepcopy(heightMap), deepcopy(heightMap), deepcopy(heightMap),deepcopy(heightMap)
        for i in range(1, m):
            for j in range(n):
                tmax[i][j] = max(heightMap[i][j], tmax[i-1][j])
        for i in range(m):
            for j in range(1, n):
                lmax[i][j] = max(heightMap[i][j], lmax[i][j-1])
        for i in range(m-2, -1, -1):
            for j in range(n):
                bmax[i][j] = max(heightMap[i][j], bmax[i+1][j])
        for i in range(m):
            for j in range(n-2, -1,-1):
                rmax[i][j] = max(heightMap[i][j], rmax[i][j+1])
        ans = 0
        print(rmax)
        for i in range(1, m-1):
            for j in range(1, n-1):
                mh = min([tmax[i-1][j], bmax[i+1][j], lmax[i][j-1], rmax[i][j+1]] )
                print(mh,  heightMap[i][j])
                ans += max(0, mh - heightMap[i][j])
        return ans
                
sol = Solution()
height = [[12,13,1,12],[13,4,13,12],[13,8,10,12],[12,13,12,12],[13,13,13,13]]
res = sol.trapRainWater(height)
print(res)