import enum
from typing import List
from collections import defaultdict


# brutal force solution
class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        numDict = {}
        for index, value in enumerate(arr):
            numDict[value] = index
        ans = 2
        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                curr = 2
               
                prev, next  = arr[i], arr[j]
                next_index = j
                while prev + next in numDict and numDict[prev + next] > next_index:
                    curr += 1
                    prev, next = next, prev + next
                    next_index = numDict[next]
                ans = max(ans, curr)
        return ans if ans >= 3 else 0
sol = Solution()
arr = [1,2,3,4,5,6,7,8]
res = sol.lenLongestFibSubseq(arr)
print(res)


# since the array is strictly increasing 
class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        S = set(arr)
        ans = 2
        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                curr = 2
                prev, next  = arr[j], arr[j] + arr[i]
                while next in S :
                    prev, next = next, prev + next
                    curr += 1
                ans = max(ans, curr)
        return ans if ans >= 3 else 0

sol = Solution()
arr = [1,2,3,4,5,6,7,8]
res = sol.lenLongestFibSubseq(arr)
print(res)

from collections import defaultdict
## dynamic programming
# longest[j, k] is the longest path ending in (j, k)
class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        index = {x: i  for i, x in enumerate(arr)}
        longest = defaultdict(lambda: 2)
        ans = 0
        for k, z in enumerate(arr):
            for j in range(k):
                i = index.get(z - arr[j], None)
                if i is not None and i < j:
                    cand = longest[j, k] = longest[i, j] + 1
                    ans = max(ans, cand)
        return ans  

sol = Solution()
arr = [1,2]
res = sol.lenLongestFibSubseq(arr)
print(res)













                




