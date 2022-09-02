from typing import List

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        m, n = len(image), len(image[0])
        scolor = image[sr][sc]
        visited = set()
        def dfs(i, j):
            visited.add((i, j))
            image[i][j] = color
            for di, dj in dirs:
                ni, nj = i+ di, j + dj
                if ni < 0 or ni >= m or nj < 0 or nj >= n:
                    continue
                tcolor = image[ni][nj]
                if (ni, nj) not in visited and tcolor == scolor:
                    dfs(ni, nj)
        dfs(sr, sc)
        return image
                