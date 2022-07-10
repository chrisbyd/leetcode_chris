from typing import List

###Brutal force
class Solution:
    def nthSuperUglyNumber(self, k: int, primes: List[int]) -> int:
        n = len(primes)
        pointers = [1 for _ in range(n)]
        dp = [1 for _ in range(k+1)]
        dp[1] = 1
        for i in range(2, k+1):
            product = [0 for _ in range(n)]
            for j, prime in enumerate(primes):
                product[j] = prime * dp[pointers[j]]
      
            dp[i] = min(product)
            for j, p in enumerate(product):
                if dp[i] == p:
                    pointers[j] += 1
        return dp[-1]

sol = Solution()

primes = [2,7,13,19]
n = 12
res = sol.nthSuperUglyNumber(n, primes)
print(res)

import heapq

class Solution1:
    def nthSuperUglyNumber(self, k: int, primes: List[int]) -> int:
        dp, heap, visited = [1], [], set()
        for index, value in enumerate(primes):
            heapq.heappush(heap, (value, index, 0))

        while len(dp) < k:
            v, prime_idx, dp_idx = heapq.heappop(heap)
            if v not in visited:
                dp.append(v)
                visited.add(v)
            heapq.heappush(heap,(primes[prime_idx]* dp[dp_idx +1], prime_idx, dp_idx+1 ))
        print(dp)
        return dp[-1]


sol = Solution1()
primes = [2,7,13,19]
n = 12
res = sol.nthSuperUglyNumber(n, primes)
print(res)
        