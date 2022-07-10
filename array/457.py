from typing import List



# wrong answer. All the numbers must be either all positive or negatives

import collections
class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        hmap = collections.defaultdict(int)
        index = 0
        count = 0
        while index not in hmap:
            hmap[index] = count
            index = (index + nums[index]) % len(nums)
            count += 1
        length = count - hmap[index]
        return True if length > 1 else False


class Solution1:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        for idx in range(len(nums)):
            hmap = collections.defaultdict(int)
            index = idx
            count = 0
            start = nums[index]
            if_break = False
            while index not in hmap:
                if nums[index] * start < 0:
                    if_break = True
                    break 
                hmap[index] = count
                index = (index + nums[index]) % len(nums)
                count += 1
            length = count - hmap[index] if not if_break else False
            if length > 1:
                return True
        return False



sol = Solution1()
nums = [3, 1, 2]
res = sol.circularArrayLoop(nums)
print(res)

class Solution2:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        visited = set()
        for i, value in enumerate(nums):
            if i in visited:
                continue
            traverse = []
            j = i
            while value * nums[j] > 0:
                if j in traverse:
                    if traverse[-1] == j:
                        break
                    else:
                        return True
                traverse.append(j)
                visited.add(j)
                j = (j+ nums[j]) % len(nums)
        return False


sol = Solution2()
nums = [3, 1, 2]
res = sol.circularArrayLoop(nums)
print(res)















