from collections import defaultdict
from typing import List

#### with cache still tle
class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        ind_dict = defaultdict(list)
        for index, num in enumerate(arr):
            ind_dict[num].append(index)
        cache = {}
        def dp(index, difference):
            if (index, difference) not in cache:
                if index == 0:
                    ans =  1
                else:
                    ans = 1
                    for idx in range(index-1, -1, -1):
                        if arr[idx] == arr[index] - difference:
                            ans = 1 + max(ans, dp(idx, difference))
                            break
                cache[index, difference] = ans
                return ans

            else:
                return cache[index, difference]
        n = len(arr)
        ans = dp(n-1, difference)
  
        for idx in range(n-2, -1, -1):
            if arr[idx] == arr[n-1] - difference :
                break
            else:
                  ans = max(dp(idx, difference), ans) 
        return ans
                    
sol = Solution()
arr = [1,5,7,8,5,3,4,2,1]
difference = -2
arr  = [3,0,-3,4,-4,7,6]
difference = 3
res = sol.longestSubsequence(arr, difference)
print(res)

#### tmd 我自杀
#### hashmap and dynamic programming
from collections import defaultdict
from typing import List
class Solution:

    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dic = defaultdict(int)
        n = len(arr)
        ans = 0
        for i in arr:
            dic[i] = 1 + dic[i - difference]
            ans = max(ans, dic[i])
        return ans
            