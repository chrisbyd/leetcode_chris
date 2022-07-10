from typing import List

class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        ans = 0
        for i in range(n):
            ans += mat[i][i]
            ans += mat[i][n-i-1]
        if n % 2 != 0:
            index = n // 2
            ans -= mat[index][index]
        return ans
    




        