from typing import List
import copy
class Solution: 
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        ans = [[0 for _ in range(n)] for _ in range(m)]
        presum = copy.deepcopy(mat)
        for i in range(m):
            cum = 0
            for j in range(n):
                cum += mat[i][j]
                presum[i][j] = cum
        for i in range(m):
            for j in range(n):
                s_i = i - k if i- k >= 0 else 0
                e_i = i+ k if i + k < m else m-1
                s_j = j - k if j - k >= 0 else 0
                e_j = j + k if j + k < n else n-1
                cum_sum = 0
                for ii in range(s_i, e_i + 1):
                    cum_sum += presum[ii][e_j] - presum[ii][s_j-1] if s_j > 0 else presum[ii][e_j]
                ans[i][j] = cum_sum
        return ans
                
## with dynamic programmming
from typing import List
import copy
class Solution: 
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        presum = copy.deepcopy(mat)
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    presum[i][j] = mat[i][j]
                elif i == 0:
                    presum[i][j] = mat[i][j] + presum[i][j-1]
                elif j == 0 :
                    presum[i][j] = mat[i][j] + presum[i-1][j]
                else:
                    presum[i][j] = mat[i][j] + presum[i][j-1] + presum[i-1][j] - presum[i-1][j-1]
        print(presum)
        ans = [[0 for j in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                s_i = i - k if i- k >= 0 else 0
                e_i = i+ k if i + k < m else m-1
                s_j = j - k if j - k >= 0 else 0
                e_j = j + k if j + k < n else n-1
                if s_i == 0 and s_j != 0:
                    res = presum[e_i][e_j] - presum[e_i][s_j - 1]
                elif s_i  != 0 and s_j == 0:
                    res = presum[e_i][e_j]  - presum[s_i-1][e_j]
                elif s_i ==0 and s_j == 0:
                    res = presum[e_i][e_j]
                else:
                    res = presum[e_i][e_j] - presum[e_i][s_j - 1] - presum[s_i-1][e_j] + presum[s_i -1][s_j -1]
                ans[i][j] = res
        return ans
mat = [[1,2,3],[4,5,6],[7,8,9]]
k = 2
sol = Solution()
res = sol.matrixBlockSum(mat, k )
print(res)
###avoid edge cases

