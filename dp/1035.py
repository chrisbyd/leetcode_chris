from typing import List

class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        m, n = len(nums1), len(nums2)
        @lru_cache(None)
        def dp(i, j):
            if i == m or j == n:
                return 0
            else:
                if nums1[i] == nums2[j]:
                    return 1 + dp(i+1, j+1)
                else:
                    return max(dp(i+1, j), dp(i, j+1))
        return dp(0, 0)
                    
                    
            
            