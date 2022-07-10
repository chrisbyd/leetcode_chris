from typing import List
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_map, heap = {}, []
        res = []
        for num in nums:
            if num not in count_map:
                count_map[num] = 1
            else:
                count_map[num] += 1
        for num in count_map:
            value, freq = num, count_map[num]
            heapq.heappush(heap,(-freq, value))
        res = []
        for _ in range(k):
            res.append(heapq.heappop(heap)[1])
        return res
        
            
        

sol = Solution()
nums = [1,1,1,2,2,3]
k = 3
res = sol.topKFrequent(nums, k)
print(res)
        