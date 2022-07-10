import imp
from typing import List

class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        if len(books) == 1:
            return books[1]
        n = len(books)
        @lru_cache(None)
        def dp(index, leftShelfWidth, curMax):
            if index == n-1:
                if books[index][0] <= leftShelfWidth:
                    return max(curMax, books[index][1])
                else:
                    return curMax + books[index][1]
                
            ans = float('inf')
            
            if books[index][0] <= leftShelfWidth:
                newCurMax = max(curMax, books[index][1])
                return min(dp(index+1, leftShelfWidth - books[index][0], newCurMax),
                          curMax + dp(index+1, shelfWidth - books[index][0], books[index][1]))
            else:
                return curMax + dp(index+1, shelfWidth - books[index][0], books[index][1])
        return dp(1, shelfWidth - books[0][0], books[0][1])