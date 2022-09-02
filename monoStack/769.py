from typing import List

class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        ans = 0
        res = [0] * len(arr)
        for i, num in enumerate(arr):
            res[num] = 1
            if sum(res[:i+1]) == i+ 1:
                ans += 1
        return ans
            
        
        