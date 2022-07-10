from typing import List
import collections
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        hmap = collections.defaultdict(int)
        for var in arr:
            hmap[var] += 1
        if len(set(hmap.values())) != len(hmap.values()):
            return False
        return True

sol = Solution()
arr = [1,2]
res = sol.uniqueOccurrences(arr)
print(res)

        