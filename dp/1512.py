from typing import List


## o(n*2)
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                if nums[i] == nums[j]:
                    ans += 1
        return ans
        
### with hashset
from collections import defaultdict
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        c_dic = defaultdict(int)
        for num in nums:
            c_dic[num] += 1
        ans = 0
        for value in c_dic.values():
            if value >= 2:
                ans += (value * (value - 1)) // 2
        return ans 
                