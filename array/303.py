from typing import List
class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        

    def sumRange(self, left: int, right: int) -> int:
        res = 0
        for i in range(left, right +1):
            res += self.nums[i]
        return res

obj = NumArray([-2,0,3,-5,2,-1])
res = obj.sumRange(2,5)
print(res)