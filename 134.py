from typing import List


# more like brutal force
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        num = len(gas)
        rd = [gas[i] - cost[i] for i in range(num)]
        sp = 0
        for i in range(sp, num):
            c_sum = 0 
            tcount = 0
            for j in range(sp,num+ sp):
                index = j % num
                c_sum += rd[index] 
                
                if c_sum < 0:
                    sp = j + 1
                    break
                tcount += 1 
            if tcount == num:
                return sp
        return -1

sol = Solution() 
gas = [4,5,2,6,5,3]
cost = [3,2,7,3,2,9]
res = sol.canCompleteCircuit(gas, cost)
print(res)

# more time saving technique
class Solution1:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_surplus, num , surplus = 0, len(gas), 0
        index = 0
        for i in range(num):
            surplus = surplus + gas[i] - cost[i]
            total_surplus += gas[i] - cost[i]
            if surplus < 0:
                index = i + 1
                surplus = 0
        return -1 if total_surplus <0 else index

sol = Solution1() 
gas = [4,5,2,6,5,3]
cost = [3,2,7,3,2,9]
res = sol.canCompleteCircuit(gas, cost)
print(res)

    