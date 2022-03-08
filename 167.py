from typing import List
from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) -1
        t_sum = numbers[l] + numbers[r] 
        while t_sum != target:
            if t_sum > target:
                r -= 1
            else:
                l += 1
            t_sum = numbers[l] + numbers[r]
        return [l+1, r+1]

sol = Solution() 
numbers = [2,7,11,15]
target = 9
res = sol.twoSum(numbers, target)
print(res)