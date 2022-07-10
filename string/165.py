from itertools import zip_longest
from typing import List

class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = version1.split(".")
        v2 = version2.split(".")
        for d1, d2 in zip_longest(v1, v2, fillvalue= 0):
            if int(d1) < int(d2):
                return -1
            elif int(d1) > int(d2):
                return 1
        return 0

sol = Solution()

version1 = "1.02.02"
version2 = "1.02.01"
res = sol.compareVersion(version1, version2)
print(res)

        