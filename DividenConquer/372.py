from typing import List
class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        def dp(nums):
            if len(nums) == 1:
                return (a % 1337) ** (nums[0]) % 1337
            else:
                return (dp(nums[:-1]) ** 10 % 1337)  * ((a**nums[-1]) % 1337) % 1337
        return dp(b)


from typing import List

class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        def dp(nums, res):
            if len(nums) == 1:
                return (res * ((a % 1337) )**nums[0]) % 1337
            else:
                res = (res * ((a % 1337) )**nums[0]) % 1337
                res =( res  ** 10) % 1337
                return dp(nums[1:], res)
        return dp(b, 1)
 
            
        
# from typing import List