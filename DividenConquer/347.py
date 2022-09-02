from typing import List
from collections import Counter
from collections import defaultdict
from heapq import heappop,heappush
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numtofreq = Counter(nums)
        freqtonum = defaultdict(list)
        for num in numtofreq:
            freq = numtofreq[num]
            freqtonum[freq].append(num)
        heap = []
        for freq in freqtonum:
            heappush(heap, -freq)
        ans = []
        while k >0:
            freq = heappop(heap)
            ans.extend(freqtonum[-freq])
            k -= len(freqtonum[-freq])
        return ans
        
        