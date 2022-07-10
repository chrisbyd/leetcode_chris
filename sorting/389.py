from typing import List


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s = sorted(list(s))
        t = sorted(list(t))
        for i in range(len(s)):
            if s[i] != t[i]:
                return t[i]
        return t[-1]


### another solution with hashmap
from collections import defaultdict
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        t_dic = defaultdict(int)
        for c in t:
            t_dic[c] += 1
        for c in s:
            t_dic[c] -= 1
        for key in t_dic.keys():
            if t_dic[key] != 0:
                return key