import re
from typing import List

class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        clips.sort(key = lambda x: (x[0], -x[1]))
        start, end = -1, 0
        ans = 0
        for new_start, new_end in clips:
            if new_start > end or end >= time:
                break
            
            if new_start > start and new_start <= end:
                if new_end < end:
                    continue
                else:
                    start = end
                    ans += 1
            end = max(end, new_end)
        return ans if end >= time else -1
                    

from collections import defaultdict
### another solution with jump game
class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        start2maxEnd = defaultdict(list)
        # for all the same start find the maximum end
        for start, end in clips:
            start2maxEnd[start] = max(start2maxEnd[start], end)
        
        #### jump game, but what is jump game
        ans = prev_limit = cur_limit = 0
        for i in range(time + 1):
            if i > cur_limit:
                return -1
            
            if i > prev_limit:
                prev_limit = cur_limit
                ans += 1
            cur_limit = max(cur_limit, start2maxEnd[i])
        return ans
        




        



            
    