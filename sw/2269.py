from typing import List

class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        s = str(num)
        ans = 0
        for i in range(k-1, len(s)):
            divisor = int(s[i - k + 1:i+1])
            if divisor != 0 and num % divisor == 0:
                ans += 1
        return ans
        