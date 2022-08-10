from typing import List


####O(N^ 3) SOLUTION, ACCPETED But it is too slow
class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        presum = [0]
        for idx, num in enumerate(arr):
            presum.append(presum[idx] ^ num)
        n = len(arr)
        ans = 0
        for i in range(n):
            for j in range(i+1, n):
                for k in range(j, n):
                    a = presum[j] ^ presum[i]
                    b = presum[k+1] ^ presum[j]
                    if a == b: 
                        ans +=1
        return ans
                    
        