from typing import List
from collections import defaultdict
class Solution:
    def frequencySort(self, s: str) -> str:
        dic1 = defaultdict(int)
        for char in s:
            dic1[char] += 1
        dic2 = defaultdict(list)
        for key in dic1.keys():
            value = dic1[key]
            dic2[value].append(key)
        freq_list = sorted(dic2.keys(), reverse= True)
        ans = ''
        for freq in freq_list:
            for char in dic2[freq]:
                ans += freq * char
        return ans
        