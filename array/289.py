from typing import List

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def get_sum(board,m,n):
            c_sum = 0
            for i in range(m-1,m+2):
                for j in range(n-1, n +2):
                    c_sum += board[i][j]
            return c_sum

        m, n = len(board) , len(board[0]) 
        new_board = [[0 for j in range(n+2)] for i in range(m+2)]
        for i in range(m):
            for j in range(n):
                new_board[i+1][j+1] = board[i][j]
        for i in range(m):
            for j in range(n):
                if board[i][j] == 0:
                    n_sum = get_sum(new_board, i+1, j+1) 
                  
                    if n_sum == 3:
                        board[i][j] = 1
                else:
                    n_sum = get_sum(new_board, i+1, j+1) - 1
           
                    if n_sum < 2 or n_sum >3:
                        board[i][j] = 0

        return board

board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
sol  = Solution()
res = sol.gameOfLife(board)
print(res)