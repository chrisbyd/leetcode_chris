from typing import List
class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        m, n = len(mat), len(mat[0])
        presum = [[0 for j in range(n+1)] for i in range(m+1)]
        for i in range(m):
            for j in range(n):
               
                presum[i+1][j+1] = mat[i][j] + presum[i+1][j] + presum[i][j+1] - presum[i][j]
                print(i, j, presum[i+1][j+1] )
        
        print(presum)
        maxlen = 0
        for i in range(1, m+1):
            for j in range(1, n+1):
                left, right = 1,  min(i, j)
                if right <= maxlen:
                    continue
                print(left, right, maxlen)
                while left <= right:
                    if right <= maxlen:
                        break
                    mid = (left + right) // 2
                    psum = presum[i][j] - presum[i - mid][j] - presum[i][j - mid] +  presum[i- mid][j- mid]
                    print(i, j, "the mid is",mid, "psum is", psum)
                    if psum > threshold:
                        right = mid - 1
                    elif psum < threshold:
                        left = mid +1 
                        maxlen = max(maxlen, mid)
                    else:
                        maxlen = max(maxlen, mid)
                        break
        return maxlen
                        
                        
sol = Solution()
# mat = [[1,1,3,2,4,3,2],[1,1,3,2,4,3,2],[1,1,3,2,4,3,2]]
# thred = 4
mat = [[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2]]
thred = 1
res = sol.maxSideLength(mat, thred)
print(res)