from typing import List

from collections import defaultdict
class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        n = len(nums)
        dic = defaultdict(int)
        for num in nums:
            dic[num] += 1
        dic2 = defaultdict(list)
        for key in dic.keys():
            freq = dic[key]
            dic2[freq].append(key)
        ans = []
        for i in range(1, n+1):
            if i in dic2:
                new_nums = sorted(dic2[i], reverse= True)
                for num in new_nums:
                    ans += i * [num]
        return ans
                    