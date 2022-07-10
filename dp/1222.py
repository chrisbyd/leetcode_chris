from typing import List

class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        directions = [ (0, -1), (0, 1), (1, 0), (-1,0),(-1, -1),(-1, 1), (1, 1), (1, -1)]
        chessboard = [[0 for j in range(8)]  for i in range(8)]
        ans = []
        for x, y in queens:
            chessboard[x][y] = 1
        for d_x, d_y in directions:
            x, y = king[0], king[1]
 
            while x >= 0 and x <= 7 and y >= 0 and y <= 7:
                if chessboard[x][y] == 1:
                    ans.append([x, y])
                    break
                else:
                    x += d_x
                    y += d_y
        return ans
                
queens = [[0,1],[1,0],[4,0],[0,4],[3,3],[2,4]]
king = [0,0]
queens = [[0,0],[1,1],[2,2],[3,4],[3,5],[4,4],[4,5]]
king = [3,3]
sol = Solution()
res = sol.queensAttacktheKing(queens, king)
print(res)