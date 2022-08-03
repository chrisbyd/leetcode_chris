from heapq import heappop, heappush
from collections import defaultdict
import bisect
from typing import List
class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        heap = []
        taskdic = defaultdict(list)
        for idx, (t, pt) in enumerate(tasks):
            taskdic[t].append([pt, idx])
        times = sorted(list(set([t for t, pt in tasks])))
        curtime, curindex = times[0], 0
        right = bisect.bisect_right(times, curtime)
        ans = []
        for idx in range(curindex, right):
            time = times[idx]
            for task in taskdic[time]:
                heappush(heap, task)
        curindex = right
     
        while heap or curindex < len(times):
            if heap:
                pt,  idx = heappop(heap)
                ans.append(idx)
                curtime = curtime + pt
            else:
                curtime = times[curindex]
            if curindex < len(times):
                right = bisect.bisect_right(times, curtime)
                for idx in range(curindex, right):
                    time = times[idx]
                    for task in taskdic[time]:
                        heappush(heap, task)
                curindex = right
        return ans

sol = Solution()
task = [[1,2],[2,4],[3,2],[4,1]]
res = sol.getOrder(task)
print(res)