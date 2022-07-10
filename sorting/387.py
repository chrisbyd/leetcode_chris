from typing import List
from collections import defaultdict
class Solution:
    def firstUniqChar(self, s: str) -> int:
        dic = defaultdict(int)
        for char in s:
            dic[char] += 1
        for index, char in enumerate(s):
            if dic[char] == 1:
                return index
        return -1