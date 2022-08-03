from typing import List
import random
import bisect
class Solution:

    def __init__(self, rects: List[List[int]]):
        self.area = []
        self.recs = rects
        for x1, y1, x2, y2 in rects:
            area = (x2 - x1 + 1) * (y2 - y1+1)
            self.area.append(area)
        self.presum = []
        cum = 0
        for a in self.area:
            cum += a
            self.presum.append(cum)
            
        

    def pick(self) -> List[int]:
        randRec = random.randint(1, self.presum[-1])
        rec_index  = bisect.bisect_left(self.presum, randRec)
        rec= self.recs[rec_index]
        x = random.randint(rec[0], rec[2])
        y = random.randint(rec[1], rec[3])
        return [x, y]
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(rects)
# param_1 = obj.pick()