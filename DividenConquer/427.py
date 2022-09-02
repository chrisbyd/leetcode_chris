
# Definition for a QuadTree node.
from typing import List
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        m = len(grid)
        presum = [[0 for j in range(m+1)] for i in range(m+1)]
        for i in range(m):
            for j in range(m):
                presum[i+1][j+1] = grid[i][j ] + presum[i+1][j] + presum[i][j+1] - presum[i][j]
        i, j = m // 2 -1, m // 2 -1
        def dp(i, j, length):
            if length == 0:
                return Node(val = grid[i][j], isLeaf = 1)
            else:
                tsum =  presum[i+1][j+1] - presum[i+ 1- length][j+1] - presum[i+1][j+1-length] + presum[i+1- length][j+1-length]
                if tsum == length* length or tsum == 0:
                    val = 1 if tsum else 0
                    return Node(val = val, isLeaf = 1)
                tl = dp(i - length // 2, j - length //2 , length //2)
                tr = dp(i - length //2, j , length //2)
                bl = dp(i , j - length //2, length //2)
                br = dp(i, j,  length //2)
                node = Node(val = 1, isLeaf = False, topLeft = tl, topRight = tr, bottomLeft = bl, bottomRight = br)
                return node
        return dp(m-1, m-1, m)
                
                
                
        
        
        
        