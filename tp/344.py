from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        length = len(s)
        left, right = 0, length -1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1