from typing import List


import sys

### time limit exceeded for sure
#### backtracking method with pruning accepted
import sys
class Solution:
    ans = sys.maxsize
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        n = len(cookies)
        def dfs(index, distribution):
            if index == n:
                self.ans = min(self.ans, max(distribution))
            else:
                for i in range(k):
                    if max(distribution) >= self.ans:
                        break
                    distribution[i] += cookies[index]
                    dfs(index + 1, distribution)
                    distribution[i] -= cookies[index]
        dfs(0, [0 for i in range(k)])
        return self.ans
                
                
                
            
                