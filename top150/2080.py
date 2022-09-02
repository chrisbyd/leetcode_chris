from collections import defaultdict
from typing import List
###MEOERY EXCEEDED
class RangeFreqQuery:

    def __init__(self, arr: List[int]):
        self.arr = arr
        self.prefix =[defaultdict(int)]
        for num in self.arr:
            prev = self.prefix[-1].copy()
            prev[num] += 1
            self.prefix.append(prev)

    def query(self, left: int, right: int, value: int) -> int:
        rdict = self.prefix[right+1]
        ldict = self.prefix[left]
        freq = rdict[value] - ldict[value]
        return freq

### throutgh binary search
from collections import defaultdict
import bisect
class RangeFreqQuery:

    def __init__(self, arr: List[int]):
        self.dict = defaultdict(list)
        for i, num in enumerate(arr):
            self.dict[num].append(i)
        
    def query(self, left: int, right: int, value: int) -> int:
        indices = self.dict[value]
        left_index = bisect.bisect_left(indices, left)
        right_index = bisect.bisect_right(indices, right)
        if left_index == right_index:
            return 0
        else:
            return right_index - left_index
        