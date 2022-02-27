from typing import List

class Solution: 
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        length = len(nums)
        for i in range(length -1):
            if nums[i] != nums[i+1]:
                if i == 0:
                    return nums[i]
                elif nums[i] != nums[i-1]:
                    return nums[i]
        return nums[length -1] 

sol = Solution()
nums = [4]
res = sol.singleNumber(nums)
print(res)
                    
            
            
from collections import Counter
class Solution1:
    def singleNumber(self, nums: List[int]) -> int:
            d = Counter(nums)
            return (min(d, key= d.get))

        