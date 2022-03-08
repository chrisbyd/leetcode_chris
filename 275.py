from typing import List

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        for index, citation in enumerate(citations):
            h = len(citations) - index
            if h <= citation:
                return h 
        return 0

sol = Solution()
citations = [1,2,2]
res = sol.hIndex(citations)
print(res)

