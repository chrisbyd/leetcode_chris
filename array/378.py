from typing import List

#brutal force solution ---Accepted---
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        list_to_sort = []
        for row in matrix:
            list_to_sort.extend(row)
        list_to_sort.sort()
        return list_to_sort[k-1]

sol = Solution()
matrix = [[1,5,9],[10,11,13],[12,13,15]]
k = 8
res = sol.kthSmallest(matrix, k)
print(res)

import heapq
class  Solution1:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        heap = []
        m, n = len(matrix), len(matrix[0])
        heapq.heappush(heap, (matrix[0][0], (0,0)))
        visited = [[0 for j in range(len(matrix[0]))] for i in range(len(matrix))]
        visited[0][0] = 1
        count = 0
        while len(heap) != 0:
            value, (i,j) = heapq.heappop(heap)
            count += 1
            if count == k:
                return value
            if i < m-1 and not visited[i+1][j]:
                to_push = (matrix[i+1][j], (i+1, j))
                visited[i+1][j] = 1
                heapq.heappush(heap, to_push)
            if j < n-1 and not visited[i][j+1]:
                visited[i][j+1] = 1
                to_push = (matrix[i][j+1], (i, j+1))
                heapq.heappush(heap, to_push)
        return -1 

sol = Solution1()
matrix = [[1,3,5],[6,7,12],[11,14,14]]
k = 6
res = sol.kthSmallest(matrix, k)
print(res)
            









