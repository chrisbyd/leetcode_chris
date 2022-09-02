from typing import List
import bisect
class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        dpmap = {}
        for i, diff in enumerate(difficulty):
            if diff not in dpmap:
                dpmap[diff] = profit[i]
            else:
                if profit[i] > dpmap[diff]:
                    dpmap[diff] = profit[i]
        difficulty.sort()
        for i in range(1, len(difficulty)):
            if dpmap[difficulty[i]] < dpmap[difficulty[i-1]]:
                dpmap[difficulty[i]] = dpmap[difficulty[i-1]]
        ans = 0
        for wo in worker:
            index = bisect.bisect_right(difficulty, wo)
            if index != 0:
                ans += dpmap[difficulty[index-1]]
        return ans