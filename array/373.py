from typing import List
import heapq
#the first brutal force solution is described as
# however it will recive MLE or toe error
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        res, heap = [], []
        for i in range(len(nums1)):
            for  j in range(len(nums2)):
                pair = [nums1[i], nums2[j]]
                to_insert = (sum(pair), pair)
                heapq.heappush(heap, to_insert)
        while k!=0 and len(heap) != 0:
            res.append(heapq.heappop(heap)[1])
            k -= 1
        return res

# sol = Solution()
# nums1 = [1,7,11]
# nums2 = [2,4,6]
# k = 3
# res = sol.kSmallestPairs(nums1, nums2, k)
# print(res)

# ok thats switch to another technique。 It is wrong saddly
class Solution1:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        i, j = 0, 0
        ans, heap, visited = [], [], set()
        ans.append([nums1[0], nums2[0]])
        visited.add((0,0))
        while  not (i == len(nums1) -1 and  j == len(nums2) - 1):
            if i == len(nums1) - 1:
                if (i,j +1) not in visited:
                    to_insert = (sum([nums1[i], nums2[j+1]]), [nums1[i], nums2[j+1]], (i, j+1))
                    visited.add((i, j+1))
                    heapq.heappush(heap, to_insert)
               
            elif j == len(nums2) - 1: 
                if (i+1,j) not in visited:
                    to_insert = (sum([nums1[i+1], nums2[j]]), [nums1[i+1], nums2[j]], (i+1, j))
                    visited.add((i+1,j))
                    heapq.heappush(heap, to_insert)
               
            else:
                if (i+1,j) not in visited:
                    to_insert1 = (sum([nums1[i+1], nums2[j]]), [nums1[i+1], nums2[j]], (i+1, j))
                    visited.add((i+1, j))
                    heapq.heappush(heap, to_insert1)
                if (i, j+1) not in visited:
                    to_insert2 = (sum([nums1[i], nums2[j+1]]), [nums1[i], nums2[j+1]], (i, j+1))
                    visited.add((i, j+1))
                    heapq.heappush(heap, to_insert2)
            _, value, (i,j) = heapq.heappop(heap)
            
            ans.append(value)
            if len(ans) == k:
                return ans
     
        return ans 
        


            
sol = Solution1()
nums1 = [1,7,11]
nums2 = [2,4,6]
k = 3
res = sol.kSmallestPairs(nums1, nums2, k)
print(res)
    






   