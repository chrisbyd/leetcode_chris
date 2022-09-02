from typing import List
from collections import Counter
class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        nums.sort()
        hmap = Counter(nums)
        if n % k != 0:
            return False
        tgroups, cgroups = n // k, 0
        sindex, start = 0, nums[0]
        while True:
            end = start + k - 1
            for num in range(start, end+ 1):
                if num not in hmap or hmap[num] == 0:
                    return False
                hmap[num] -= 1
            cgroups +=  1
            if cgroups == tgroups:
                return True
            while sindex < n:
                start = nums[sindex]
                if hmap[start] != 0:
                    break
                sindex += 1
                
            