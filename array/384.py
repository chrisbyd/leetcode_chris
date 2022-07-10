import imp
from typing import List
import random
class Solution:

    def __init__(self, nums: List[int]):
        self.original_nums = nums
        self.cur_nums = nums
        

    def reset(self) -> List[int]:
        self.cur_nums = self.original_nums
        return self.cur_nums
        

    def shuffle(self) -> List[int]:
        n = len(self.original_nums)
        ans = []
        existing_nums = self.original_nums[:]
        for i in range(n):
            rand_idx = int(len(existing_nums) * random.random())
            rand_value = existing_nums[rand_idx]
            ans.append(rand_value)
            existing_nums.remove(rand_value)
        return ans


 
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()

nums = [1,2,3]
sol = Solution(nums)
for i in range(100):
    ans = sol.shuffle()
    print(ans)