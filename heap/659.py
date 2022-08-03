from heapq import heappush, heappop
from typing import List

class PriorityEntry(object):
    def __init__(self, data):
        self.data = data
    
    def __lt__(self, entry):
        if self.data[1] < entry.data[1] :
            return True
        elif self.data[1] > entry.data[1]:
            return False
        else:
            return self.data[1] - self.data[0] - entry.data[1] + entry.data[0] < 0
    
class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        heap = []
        for num in nums:
            while heap and heap[0].data[1] < num - 1:
                left, right = heappop(heap).data
                if right - left < 2:
                    return False
            printHeap(heap, num)
            if heap and heap[0].data[1] == num - 1:
                left, right = heappop(heap).data
                heappush(heap, PriorityEntry([left, num]))
            else:
                heappush(heap, PriorityEntry([num, num]))
            printHeap(heap,num)
        while heap:
            left, right = heappop(heap).data
            if right - left < 2:
                return False
        return True

def printHeap(heap, num):
    ans = []
    for item in heap:
        ans.append(item.data)
    print(ans, num)

            
sol = Solution()
nums = [1,2,3,3,4,5,6,7,8]
res = sol.isPossible(nums)
print(res)