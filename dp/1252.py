class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        origin = [[0]*n for i in range(m)]
        for index_i, index_j in indices:
            for j in range(n):
                origin[index_i][j] += 1
            for i in range(m):
                origin[i][index_j] += 1
        ans = 0
        for i in range(m):
            for j in range(n):
                if origin[i][j] % 2 != 0:
                    ans += 1
        return ans
                