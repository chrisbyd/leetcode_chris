from typing import List
import collections
class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        else:
            res = self.countAndSay(n-1)
            prev = res[0]
            count = 1
            ans = ''
            for i in range(1, len(res)):
                if res[i] != prev:
                    ans += ( str(count) + prev)
                    count = 1 
                    prev = res[i]
                else:
                    count += 1
            ans += (str(count) + prev)
            return ans

sol = Solution()
n = 5
res = sol.countAndSay(n)
print(res)


# another implementation of the algorithm