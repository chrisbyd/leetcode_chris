from typing import List
from typing import List
### tle error
class Solution:
    def constructArray(self, n: int, k: int) -> List[int]:
        def dfs(mask, res, unique):
            if mask == (1 << n) - 1 and len(unique) == k:
                return res
            for i in range(n):
                if (mask >> i) & 1 == 0:
                    if  res:
                        if abs((i+1) - res[-1]) not in unique:
                            unique.add(abs((i+1) - res[-1]))
                            if len(unique) <=k:
                                ans = dfs(mask | (1 << i), res + [i+1], unique)
                                if ans:
                                    return ans
                            unique.remove(abs((i+1) - res[-1]))
                        else:
                            ans = dfs(mask | (1 << i), res + [i+1], unique)
                            if ans:
                                return ans

                    else:
                        ans = dfs(mask| (1 <<i), [i+1], unique)
                        if ans:
                            return ans
            return False
        return dfs(0, [], set())

sol = Solution()
n = 3
k = 2
res = sol.constructArray(n, k)
print(res)
#### another solution
### from the answer which is definately accepted

from typing import List
from typing import List

#### a solution by construction
###how do u come up with this solution 

class Solution:
    def constructArray(self, n: int, k: int) -> List[int]:
        ans = list(range(1, n - k ))
        for i in range(k +1):
            if i % 2 == 0 :
                ans.append(n - k + i // 2 )
            else:
                ans.append(n - i // 2)
        return ans
            


























