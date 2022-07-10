from typing import List

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n+1))
    
    def root(self, a):
        if self.parent[a] == a:
            return a
        else:
            p = self.parent[a]
            return self.root(p) 

    def  union(self, a, b):
        a_root = self.root(a)
        b_root = self.root(b)
        self.parent[b_root] = self.parent[a_root]
    
    def find(self, a, b):
        if self.root(a) == self.root(b):
            return True
        return False
 
class Solution:

    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        Uf = UnionFind(m * n)
        for i in range(m):
            if board[i][0] == 'O':
                Uf.union(0, i*n+1)
            if board[i][n-1] == 'O':
                Uf.union(0, (i + 1)*n )
        for j in range(n):
            if board[0][j] == 'O':
                Uf.union(0, j+1)
            if board[m-1][j] == 'O':
                Uf.union(0, n*m -n +j +1)
        directions = [(0,1),(0,-1),(-1,0),(1,0)]
        for i in range(1, m -1):
            for j in range(1, n-1):
                if board[i][j] == 'O':
                    for a, b in directions:
                        x, y = i + a, j + b
                        if board[x][y] == 'O':
                            Uf.union(i*n+j+1, x*n+y+1)
        
        for i in range(1, m-1):
            for j in range(1, n-1):
                if board[i][j]  == 'O':
                    if not Uf.find(0, i*n +j+1):
                        board[i][j] = 'X'
        

sol = Solution()

board = [["O","O","O","O","X","X"],["O","O","O","O","O","O"],["O","X","O","X","O","O"],["O","X","O","O","X","O"],["O","X","O","X","O","O"],["O","X","O","O","O","O"]]
board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
sol.solve(board)
print(board)



class Solution1:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m ,n = len(board), len(board[0])
        def dfs(i, j):
            if i < 0 or i > m-1 or j<0 or j > n-1 or board[i][j] != 'O':
                return
            board[i][j] = 'E'
            dfs(i-1, j)
            dfs(i+1, j)
            dfs(i, j-1)
            dfs(i, j+1)
        for i in range(m):
            dfs(i, 0)
            dfs(i, n-1)
        for j in range(n):
            dfs(0, j)
            dfs(m-1, j)
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'E':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'

sol = Solution1()

board = [["O","O","O","O","X","X"],["O","O","O","O","O","O"],["O","X","O","X","O","O"],["O","X","O","O","X","O"],["O","X","O","X","O","O"],["O","X","O","O","O","O"]]
board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
sol.solve(board)
print(board)
