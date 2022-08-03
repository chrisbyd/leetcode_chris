from typing import List

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        count_1 = 0
        index = -1
        for i in range(32):
            if (n >> i) & 1:
                count_1 += 1
                index = i
        if count_1 != 1: return False
        elif index % 2 != 0:
            return False
        return True
            
        