from typing import List

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        nhand = sorted(hand)
        while nhand:
            start = nhand[0]
            for i in range(groupSize):
                rem = start + i
                if rem not in nhand:
                    return False
                nhand.remove(rem)
        return True
       
from typing import List
import bisect
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        nhand = sorted(hand)
        while nhand:
            start = nhand[0]

            for i in range(groupSize):
                rem = start + i
                index = bisect.bisect_left(nhand, rem)
                if index >= len(nhand) or   nhand[index] !=  rem:
                    return False
                else:
                    nhand = nhand[:index] + nhand[index + 1: ]
        return True
       
from typing import List
import bisect
from collections import Counter
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        hand, n = sorted(hand), len(hand)
        if  n % groupSize != 0 :
            return False
        tgroups = n // groupSize
        hmap = Counter(hand)
        start = hand[0]
        sindex = 0
        cgroups = 0
        while True:
            for i in range(groupSize):
                num = start + i
                if num not in hmap or hmap[num] == 0:
                    return False
                else:
                    hmap[num] -= 1
            cgroups += 1
            if cgroups == tgroups:
                return True
            while sindex < n:
                start = hand[sindex]
                if hmap[start] != 0:
                    break
                sindex += 1
        return True
       
        
        
        