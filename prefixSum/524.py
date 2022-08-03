from typing import List

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        maxlen, count, n = 0,  0, len(nums)
       
        seen = {0: -1}
        for i in range(n):
            count = count + 1 if nums[i] == 1 else count - 1
            if count not in seen:
                seen[count] = i
            else:
                maxlen  = max(maxlen, i - seen[count])
        return maxlen


