from typing import List

# class Solution:
#     def hIndex(self, citations: List[int]) -> int:
#         citations.sort()
#         for idx, h in enumerate(citations):
#             if h == len(citations[idx:]):
#                 return h 
        



class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        for index,value in enumerate(citations):
            if index>=value:
                return index
        return(len(citations))

citations = [3,0,6,1,5]
sol = Solution()
res = sol.hIndex(citations)
print(res)