from collections import defaultdict
from typing import List
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num2freq = defaultdict(int)
        heap = []
        for num in nums:
            num2freq[num] += 1
        for key in num2freq.keys():
            heapq.heappush(heap, (-num2freq[key], key))
        ans = []
        for i in range(k):
            ans.append(heapq.heappop(heap)[1])
        return ans
            
        
        
sol = Solution()
nums = [1,2]
res = sol.topKFrequent(nums, 2)
print(res)