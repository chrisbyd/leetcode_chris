from typing import List



##dfs + pruning
class Solution:
    def minimizeTheDifference(self, mat: List[List[int]], target: int) -> int:
        
        n = len(mat)
        @lru_cache(None)
        def dp(row, c_sum):
            if row == n:
                return abs(c_sum - target)
            else:
                ans = float('inf')
                for num in mat[row]:
                    ans = min(ans, dp(row+1, c_sum + num))
                    if c_sum + num >= target:
                        break
                    
                return ans
        for i in range(n):
            mat[i] = sorted(set(mat[i]))
        return dp(0, 0)
                     
                
                
            