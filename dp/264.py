from typing import List
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        final = {1}
        cur = {1}
        while len(final) < 5000:
            tem = set()
            for i in cur:
                tem.add(2 * i)
                tem.add(3* i)
                tem.add(5 * i)
            final.update(tem)
            cur = tem
        final = sorted(list(final))
        print(final[n-1])
        return final[n-1]

sol = Solution()
n = 10
res = sol.nthUglyNumber(n)
print(res)
