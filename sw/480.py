from heapq import heappop, heappush
from typing import List
import bisect
class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        def median(array, i, j):
            return (array[i] + array[j]) / 2
        if k % 2 == 0:
            i , j = k //2 -1,  k //2
        else:
            i, j = k // 2, k //2
        
        array = nums[: k]
        array.sort()
        ans = []
        for r in range(k, len(nums)):
            med = median(array, i, j)
            ans.append(med)
            array.remove(nums[r - k])
            bisect.insort(array, nums[r])
        ans.append(median(array, i, j))
        return ans
            
            