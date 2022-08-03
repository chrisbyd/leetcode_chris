from  typing import List
import random
import bisect
class Solution:

    def __init__(self, w: List[int]):
        self.weight = w
        self.presum = []
        cum = 0
        for w in self.weight:
            cum += w
            self.presum.append(cum)
            

    def pickIndex(self) -> int:
        rand = random.randint(1, self.presum[-1])
        return bisect.bisect_left(self.presum, rand)

