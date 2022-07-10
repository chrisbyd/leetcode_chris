from typing import List

from collections import defaultdict
class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        length = len(nums)
        dic = defaultdict(int)
        for num in nums:
            dic[num] += 1
        for val in dic.values():
            if val % 2 != 0:
                return False
        return True
        