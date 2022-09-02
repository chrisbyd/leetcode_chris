from typing import List
from collections import Counter
class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self. nums1 = nums1
        self.nums2 = nums2
        self.cmap = Counter(nums1)
        

    def add(self, index: int, val: int) -> None:
        self.nums2[index] += val

    def count(self, tot: int) -> int:
        ans = 0
        for num in self.nums2:
            remain = tot - num
            ans += self.cmap[remain]
        return ans
        


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)
####optimized accpted
from typing import List
from collections import Counter
class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums2 = nums2
        self.cmap = Counter(nums1)
        self.nums2map = Counter(nums2)
        self.distinctNums1 = set(self.cmap.keys())
        

    def add(self, index: int, val: int) -> None:
        origin = self.nums2[index]
        self.nums2map[origin] -=1
        self.nums2map[origin + val] += 1
        self.nums2[index] += val

    def count(self, tot: int) -> int:
        ans = 0
        for num in self.distinctNums1:
            remain = tot - num
            ans += self.cmap[num] * self.nums2map[remain]
        return ans
        


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)