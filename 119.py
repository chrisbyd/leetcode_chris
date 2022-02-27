from typing import List

class Solution:
    def getRow(self, rowIndex: int) -> List[List[int]]:
        res = []
        for i in range(rowIndex+1):
            n_row = []
            res.append(n_row)
            for j in range(i+1):
                if j == 0 or j == i:
                    n_row.append(1)
                else:
                    n_row.append(res[i-1][j]+ res[i-1][j-1])
        return res[rowIndex]

sol = Solution()
rowIndex = 3
print(sol.getRow(rowIndex))
