import imp
from typing import List
import collections
# o(n^2) Accepted
class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        index_map = collections.defaultdict(int)
        for idx, interval in enumerate(intervals):
            index_map[interval[0], interval[1]] = idx
        
        intervals.sort(key= lambda x: x[0])
        ans = [0 for i in range(len(intervals))]
        for i in range(len(intervals)):
            find = False
            for inter in intervals[i:]:
                if inter[0] >= intervals[i][1]:
                    ans[index_map[intervals[i][0], intervals[i][1]]] = index_map[inter[0], inter[1]]
                    find = True
                    break
            if not find:
                ans[index_map[intervals[i][0], intervals[i][1]]] = -1
        
        return ans

sol = Solution()
intervals = [[1,1],[3,4]]

res = sol.findRightInterval(intervals)
print(res)


            






        