from typing import List
class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        dirs = [(1, 0 ), (-1, 0), (0,1), (0, -1), (-1, 1), (-1,-1), (1, -1), (1, 1)]
        m, n = len(board), len(board[0])
        def dfs(i,j ):
            if board[i][j] == 'M':
                board[i][j] = 'X'
                return
            elif board[i][j] == 'E':
                count = 0
                for di, dj in dirs:
                    if i+ di >=0 and i+di <m and j+dj >=0 and j+dj <n and board[i+di][j +dj] == 'M':
                        count += 1
                if count != 0:
                    board[i][j] = str(count)
                else:
                    board[i][j] = 'B'
                    for di, dj in dirs:
                        if i+ di >=0 and i+di <m and j+dj >=0 and j+dj <n:
                            dfs(i+di, j + dj)
        dfs(click[0], click[1])
        return board
        