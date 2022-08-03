from typing import List

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            stones = sorted(stones)
            if stones[-1] - stones[-2] != 0:
                stones = stones[:-2] + [stones[-1] - stones[-2]]
            else:
                stones = stones[:-2]
        if not stones:
            return 0
        return stones[0]
        