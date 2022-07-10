from typing import List

from torch import maximum

# the solution by myself
# still requires some endeavour
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        intervals = []
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                intervals.append([prices[i-1], prices[i]])
        n = len(intervals)
        dp = [[0 for j in range(n)] for i in range(n)]
        def dp(i, j):
            if i == j:
                return intervals[i][1] - intervals[i][0]
            else:
                pass

       
        

prices = [3,3,5,0,0,3,1,4]
prices = [1,2,3,4,5]
prices = [7,6,5,4,3,2,1]
prices = [6,1,3,2,4,7]
prices = [1,2,4,2,5,7,2,4,9,0]
sol = Solution()
res = sol.maxProfit(prices)
print(res)

# a more delicate solution    
            

# divide and conquer o(N2)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        def find_maxmum(prices):
            if len(prices) == 0:
                return 0
            ans = 0
            start = prices[0]
            for i in range(1, len(prices)):
                if prices[i] < start:
                    start = prices[i]
                ans = max(prices[i]- start, ans)
            return ans
        ans = 0
        for i in range(len(prices)):
            #solve left
            left = find_maxmum(prices[:i])
            right = find_maxmum(prices[i:])
            ans = max(ans, left + right)
        return ans

sol = Solution()
prices = [1,2,3,4,5]
res = sol.maxProfit(prices)
print(res)

#  divide and conquer o(n)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = [0 for i in range(len(prices))]
        right = [0 for i in range(len(prices))]
        buy = prices[0]
        ans = 0
        for i in range(len(prices)):
            if prices[i] < buy:
                buy = prices[i]
            ans = max(ans, prices[i] - buy)
            left[i] = ans
        
        sell = prices[-1]
        ans = 0
        for i in range(len(prices) -1, -1, -1):
            if prices[i] > sell:
                sell = prices[i]
            ans = max(ans, sell - prices[i])
            right[i] = ans
        ans = []
        for i in range(len(left)):
            ans.append(left[i] + right[i])
        return max(ans)


sol = Solution()
prices = [3,3,5,0,0,3,1,4]
res = sol.maxProfit(prices)
print(res)