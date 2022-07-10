from typing import List
####
####exhaustive search
class Solution:
    count = 0
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        
        def search(n, target):
            if n == 1:
                if target <= 0 or target > k:
                    return 0
                else:
                    self.count += 1
            else:
                for i in range(1, k+1):
                    search(n-1, target - i)
        search(n, target)
        return self.count % (10 ** 9 + 7)

### accepted        
class Solution:
    count = 0
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        @lru_cache(None)
        def search(n, target):
            if n == 1:
                if target <= 0 or target > k:
                    return 0
                else:
                    return 1
            else:
                ans = 0
                for i in range(1, k+1):
                    ans += search(n-1, target - i)
                return ans
        res = search(n, target)
        return res % (10 ** 9 + 7)
                    
                