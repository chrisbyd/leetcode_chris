from typing import List


# brutal force solution
class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        def dp(curr_needs, cost):
     
            if set(curr_needs) == {0}:
                return cost
            elif min(curr_needs) < 0:
                return float('inf')
            else:
                cost1 = 0 
                for i in range(len(curr_needs)):
                    cost1 += price[i] * curr_needs[i]
            
                ans = cost1 + cost

                for spc in special:
                    if sum(spc[:-1]) != 0:
                        ans = min(ans, dp([curr_needs[i] - spc[i] for i in range(len(needs))], spc[-1] + cost))
           
                return ans
        return dp(needs, 0)


sol = Solution()
price = [2,5]
special = [[3,0,5],[1,2,10]]
needs = [3,2]
res = sol.shoppingOffers(price, special, needs)
print(res)

                

# brutal force solution
# with 
class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        memo = {}
        def dp(curr_needs, cost):
            if tuple(curr_needs + [cost]) not in memo:
                if set(curr_needs) == {0}:
                    res =  cost
                elif min(curr_needs) < 0:
                    res =  float('inf')
                else:
                    cost1 = 0 
                    for i in range(len(curr_needs)):
                        cost1 += price[i] * curr_needs[i]
                
                    ans = cost1 + cost

                    for spc in special:
                        if sum(spc[:-1]) != 0:
                            ans = min(ans, dp([curr_needs[i] - spc[i] for i in range(len(needs))], spc[-1] + cost))
                    res = ans
                memo[tuple(curr_needs + [cost])] = res
                return res
            else:
                return memo[tuple(curr_needs + [cost])]
        return dp(needs, 0)


sol = Solution()
price = [2,5]
special = [[3,0,5],[1,2,10]]
needs = [3,2]
res = sol.shoppingOffers(price, special, needs)
print(res)   