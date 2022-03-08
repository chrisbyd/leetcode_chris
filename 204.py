from typing import List
import math
class Solution:
   
    def countPrimes(self, n: int) -> int:
        if n ==0:
            return 0
        primes = [1 for _ in range(n+1)]
        primes[0] = 0 
        primes[1] = 0
        s_n = math.sqrt(n)
        for i in range(2, int(s_n)+1):
            if primes[i]:
                for index in range(2*i, n+1, i):
                    primes[index] = 0
        return sum(primes[:-1])
    
sol = Solution()
n = 10
res = sol.countPrimes(2)
print(res)
