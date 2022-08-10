from typing import List
from typing import List

class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        presum, n  = [0], len(customers)
        all_presum = [0]
        for i, customer in enumerate(customers):
            if grumpy[i]:
                presum.append(presum[-1])
            else:
                presum.append(customer + presum[-1])
            all_presum.append(customer + all_presum[-1])
        ans = 0
        for i in range(minutes - 1, n ): 
            res = presum[i - minutes + 1 ] + presum[-1] - presum[i+1]
            res += all_presum[i+1] - all_presum[i+1 - minutes]
            ans = max(ans, res)
        return ans
        
        