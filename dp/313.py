from typing import List
import heapq

class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        dp, heap, visited = [1], [], set()
        for i, p in enumerate(primes):
            heapq.heappush(heap, (p, i, 0))

        while len(dp) < n:
            val, prime_idx, dp_idx = heapq.heappop(heap)
            if val not in visited:
                dp.append(val)
                visited.add(val)
            heapq.heappush(heap, (primes[prime_idx] * dp[dp_idx + 1], prime_idx, dp_idx + 1))
        return dp[-1]
                


class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        dp, heap, visited = [1], [], set()
        for i, p in enumerate(primes):
            heapq.heappush(heap, (p, i, 0))
        
        while len(dp) < n:
            val, prime_idx, dp_idx = heapq.heappop(heap)
            if val not in visited:
                dp.append(val)
                visited.add(val)
            heapq.heappush(heap, (primes[prime_idx] * dp[dp_idx + 1], prime_idx, dp_idx + 1))
        
        return dp[-1]
