from locale import AM_STR
from typing import List
from collections import deque
import collections
import heapq
# TLE
class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        length = len(nums1)  
        nums3.sort()
        nums4.sort()
        ans = 0
        for i in range(length):
            for j in range(length):
                res =  0 - nums1[i] - nums2[j]
                value = nums3[0] + nums4[0]
                heap = []
                heapq.heappush(heap, (value, (0,0)))
                visited = collections.defaultdict(int)
                visited[0,0] =1 
                while len(heap) != 0:
                    value, (m, n) = heapq.heappop(heap)
                    if value == res:
                        ans += 1
                    if value > res:
                        break
                    else:
                        if m != length -1 and n != length - 1:
                            if not visited[m+1, n]:
                                heapq.heappush(heap, (nums3[m+1] +nums4[n] , (m+1, n)))
                                visited[m+1, n] =1
                            if not visited[m, n+1]:
                                heapq.heappush(heap, (nums3[m] +nums4[n+1] , (m, n+1)))
                                visited[m, n+1] = 1
                        elif m == length -1 and n != length - 1:
                            if not visited[m, n+1]:
                                heapq.heappush(heap, (nums3[m] + nums4[n+1], (m, n+1)))
                                visited[m, n+1] = 1
                        elif m != length -1 and n == length -1:
                            if not visited[m+1, n]:
                                heapq.heappush(heap, (nums3[m+1] + nums4[n], (m+1, n)))
                                visited[m+1, n] = 1

        return ans

                            
nums1 = [0,1,-1]
nums2 = [-1,1,0]
nums3 = [0,0,1]
nums4 = [-1,1,1]
sol = Solution()
res = sol.fourSumCount(nums1, nums2, nums3, nums4)
print(res)

                

                
import collections
#Okay an supoer easy solution with O(n^2)
class Solution1:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        n = len(nums1)
        hmap = collections.defaultdict(int)
        for i in range(n):
            for j in range(n):
                psum = nums1[i] + nums2[j]
                hmap[psum] += 1
        ans = 0
        for i in range(n):
            for j in range(n):
                psum = -(nums3[i] + nums4[j])
                ans += hmap[psum]
        return ans



nums1 = [0,1,-1]
nums2 = [-1,1,0]
nums3 = [0,0,1]
nums4 = [-1,1,1]
sol = Solution1()
res = sol.fourSumCount(nums1, nums2, nums3, nums4)
print(res)
