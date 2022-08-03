# o(n)^2
from typing import List

class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        def hamming(a, b):
            res = a^ b
            res_list = [int(v) for v in bin(res)[2:]]
            return sum(res_list)
        ans = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                ans += hamming(nums[i], nums[j])
        return ans



# with bit o(n)
class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        ans = 0
        for i in range(32):
            count_1 = 0
            for j in range(len(nums)):
                if (nums[j] >> i) & 1:
                    count_1 += 1
            ans += count_1 * (len(nums) - count_1)
        return ans