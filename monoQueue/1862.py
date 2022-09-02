from typing import List
from collections import Counter
#### tle
class Solution:
    def sumOfFlooredPairs(self, nums: List[int]) -> int:
        n = len(nums)
        ans = n
        counter = Counter(nums)
        distinct_n = len(counter.keys())
        dis_nums = sorted(list(counter.keys()))
        for i in range(distinct_n):
            for j in range(i+1, distinct_n):
                res = int(dis_nums[j] / dis_nums[i]) *(counter[dis_nums[i]] * counter[dis_nums[j]])
                ans += res
     
        for freq in counter.values():
           
            ans += (freq * (freq-1)) 
        return ans % (10 **9 + 7)
nums = [7,7,7,7,7,7,7]
res = sol.sumOfFlooredPairs(nums)
print(res)

class Solution:
    def sumOfFlooredPairs(self, nums: List[int]) -> int:
        ans, hi, n, c = 0, max(nums)+1, len(nums), Counter(nums)
        pre = [0] * hi
        for i in range(1, hi):
            pre[i] = pre[i-1] + c[i]
        for num in set(nums):
            for i in range(num, hi, num):
                ans += c[num] * (pre[-1] - pre[i-1])
        return ans % (10**9 + 7)


class Solution:
    def sumOfFlooredPairs(self, nums: List[int]) -> int:
        ans, hi, n, c = 0, max(nums)+1, len(nums), Counter(nums)
        pre = [0] * hi
        for i in range(1, hi):
            pre[i] = pre[i-1] + c[i]
        for num in set(nums):
            count = 1
            for i in range(num, hi, num):
                higher = i + num if i + num <= hi else hi
                ans += c[num] * (pre[higher-1] - pre[i-1]) * count
                count += 1
            
        return ans % (10 **9 + 7)