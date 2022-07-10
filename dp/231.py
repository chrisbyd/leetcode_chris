import math
### seems we could not use math module ok

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        logn = int(math.log(n, 2))
        if 2 ** logn == n:
            return True
        return False

sol = Solution()
n = 64
res = sol.isPowerOfTwo(n)
print(res) 


### seems we could not use math module ok


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        for i in range(32):
            if 2** i == n:
                return True
        return False
        
        
        