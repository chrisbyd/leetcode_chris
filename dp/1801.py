from typing import List
import heapq
import math
class Solution:
    def getNumberOfBacklogOrders(self, orders: List[List[int]]) -> int:
        buy_order = []
        sell_order = []
        for order in orders:
            if order[2] == 0:
                while sell_order and order[1] and sell_order[0][0] <= order[0]:
                    if sell_order[0][1] <= order[1]:
                        order[1] -= sell_order[0][1]
                        heapq.heappop(sell_order)
                    else:
                        sell_order[0][1] -= order[1]
                        order[1] = 0
                if order[1] != 0:
                    heapq.heappush(buy_order, [-order[0], order[1]])
            else:
                while buy_order and order[1] and -buy_order[0][0] >= order[0]:
                    if buy_order[0][1] <= order[1]:
                        order[1] -= buy_order[0][1]
                        heapq.heappop(buy_order)
                    else:
                        buy_order[0][1] -= order[1]
                        order[1] = 0
                if order[1] != 0:
                    heapq.heappush(sell_order, [order[0], order[1]])
        
        ans = 0
        for order in buy_order + sell_order:
            ans += order[1]
        return int(ans % (math.pow(10, 9) + 7))
        
sol = Solution()
orders = [[10,5,0],[15,2,1],[25,1,1],[30,4,0]]
orders = [[7,1000000000,1],[15,3,0],[5,999999995,0],[5,1,1]]

res = sol.getNumberOfBacklogOrders(orders)
print(res)