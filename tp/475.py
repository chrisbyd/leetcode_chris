from typing import List, Optional

import bisect
class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters.sort()
        ans = -float('inf')
        length = len(heaters)
        for pos in houses:
            index = bisect.bisect_left(heaters, pos)
            if index == 0:
                ans = max(ans,  heaters[0] - pos)
            elif index == length:
                ans = max(ans,  pos - heaters[-1])
            else:
                minimum = min( heaters[index] - pos, pos - heaters[index-1])
                ans = max(minimum, ans)
        return ans
        
        