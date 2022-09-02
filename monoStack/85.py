from typing import List
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or len(matrix) == 0:
            return 0
        m, n = len(matrix), len(matrix[0])
        grid = [ [int(matrix[i][j]) for j in range(n)] for i in range(m)]
        ans = 0
        for i in range(1 , m):
            for j in range(n):
                if matrix[i][j] == '1':
                    grid[i][j] = 1 + grid[i-1][j]
        
        
        def solveLargestRecHistogram(heights):
            stack, ans = [], 0
            for i, height in enumerate(heights):
                index = i
                while stack and stack[-1][1] > height:
                    index, hei = stack.pop()
                    ans = max(ans , (i - index)* hei)
                stack.append((index, height))
            n = len(heights)
            while stack:
                index, hei = stack.pop()
                ans = max((n - index) * hei, ans)
            return ans
        
        for i in range(m):
            ans = max(ans, solveLargestRecHistogram(grid[i]) )
        return ans
                
                
         