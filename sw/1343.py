from typing import List

class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        cumsum = sum(arr[:k-1])
        n = len(arr)
        ans = 0
        start = 0
        for i in range(k-1, n):
            cumsum += arr[i]
            if cumsum / k >= threshold:
                ans += 1
            cumsum -= arr[start]
            start += 1
        return ans
        