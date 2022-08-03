import copy
from typing import List

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        m, n = len(matrix), len(matrix[0])
        self.presum  = [ [0 for j in range(n+1)] for i in range(m+1)]
        for i in range(m):
            for j in range(n):
                self.presum[i+1][j+1] = matrix[i][j] + self.presum[i][j+1] + self.presum[i+1][j] - self.presum[i][j]
                

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        ans = self.presum[row2+1][col2+1] - self.presum[row2+1][col1] - self.presum[row1][col2+1] + self.presum[row1][col1]
        return ans