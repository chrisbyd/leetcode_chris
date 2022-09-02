from typing import List

class Solution:
    def maxTrailingZeros(self, grid: List[List[int]]) -> int:
        def convert(num):
            count2, count5 = 0, 0
            while num:
                if num % 2 == 0:
                    count2 += 1
                    num = num // 2
                else:
                    break
            while num:
                if num % 5 == 0:
                    count5 += 1
                    num = num // 5
                else:
                    break
            return count2, count5
        
        m, n = len(grid), len(grid[0])
        dprow = [[[0, 0] for j in range(n+1)]  for i in range(m+1)]
        dpcol   = [[[0, 0] for j in range(n+1)] for i in range(m+1)]
        for i in range(m):
            for j in range(n):
                num2s, num5s = convert(grid[i][j])
                dprow[i+1][j+1] = [dprow[i+1][j][0] + num2s, dprow[i+1][j][1] + num5s]
        for j in range(n):
            for i in range(m):
                num2s, num5s = convert(grid[i][j])
                dpcol[i+1][j+1] = [dpcol[i][j+1][0] + num2s, dpcol[i][j+1][1] + num5s]
        ans = 0
        print(dprow)
        print(dpcol)
        for i in range(m):
            for j in range(n):
                #above
                above2s, above5s = dpcol[i+1][j+1]
                below2s, below5s = dpcol[-1][j+1][0] - dpcol[i][j+1][0], dpcol[-1][j+1][1] - dpcol[i][j+1][1]
                left2s, left5s = dprow[i+1][j]
                right2s, right5s = dprow[i+1][-1][0] - dprow[i+1][j+1][0], dprow[i+1][-1][1] - dprow[i+1][j+1][1]
                res = [ [above2s + left2s, above5s + left5s], [above2s + right2s, above5s + right5s], [below2s + left2s, below5s + left5s], [below2s + right2s, below5s + right5s]]
                for n2s, n5s in res:
                    print(i, j, "and", n2s, n5s)
                    ans = max(ans, min(n2s, n5s))
        return ans

sol = Solution()
nums = [[899,727,165,249,531,300,542,890],[981,587,565,943,875,498,582,672],[106,902,524,725,699,778,365,220]]
res = sol.maxTrailingZeros(nums)
print(res)