from typing import List

#through sorting the intervals first
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key= lambda x: x[0])
        count = 0
        end = 0
        for idx, inter in enumerate(intervals):
            if idx == 0:
                end = inter[1]
            elif inter[0] < end:
                count += 1
                if inter[1] < end:
                    end = inter[1]
            else:
                end = inter[1]
        return count

sol = Solution()
intervals = [[0,2],[1,3],[2,4],[3,5],[4,6]]
res = sol.eraseOverlapIntervals(intervals)
print(res)




        