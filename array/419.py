from typing import List


class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        count = 0
        m, n = len(board), len(board[0])
        directions = [(0,1), (1, 0)]
        visited = [[0 for j in range(n)] for i in range(m)]
        def dfs(i, j):
            if i >= m or j >= n:
                return
            elif board[i][j] != 'X':
                return
            elif not visited[i][j]:
                visited[i][j] = 1
                for a, b in directions:
                    dfs(i+a, j+b)
        count = 0
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'X' and not visited[i][j]:
                    count += 1
                    dfs(i, j)
        return count




sol = Solution()
board = [["X",".",".","X"],[".",".",".","X"],[".",".",".","X"]]
res = sol.countBattleships(board)
print(res)
 
class Solution1:
    def countBattleships(self, board: List[List[str]]) -> int:
        m, n = len(board), len(board[0])
        ans = 0
        for i in range(m):
            for j in range(n):
                if board[i][j] == "X":
                    visited = False
                    if i > 0 and board[i -1][j] == 'X':
                        visited = True
                    if j > 0 and board[i][j-1] == "X":
                        visited = True
                    if not visited:
                        ans += 1
        return ans

                    


sol = Solution1()
board = [["X",".",".","X"],[".",".",".","X"],[".",".",".","X"]]
res = sol.countBattleships(board)
print(res)

        