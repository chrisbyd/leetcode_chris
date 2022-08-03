# class Solution:
#     def nextGreaterElement(self, n: int) -> int:
#         v_list = []
#         while n:
#             digit = n % 10
#             n = n //  10
#             v_list.append(digit)
#         v_list = v_list[::-1]
#         left = len(v_list) - 1
#         prev = v_list[-1]
#         for i in range(len(v_list)-2, -1, -1):
      
#             if v_list[i] < prev:
#                 left  = i
#                 break
#             else:
#                 prev = v_list[i]
#         print(left)
#         if left == len(v_list) - 1:
#             return -1
        
#         for i in range(len(v_list) -1,  left, -1):
#             if v_list[i] > v_list[left]:
#                 right = i
#                 break
#         v_list[left], v_list[right] = v_list[right], v_list[left]
#         n_v_list = v_list[:left+ 1] + sorted(v_list[left+1:])
#         ans = 0
#         for v in n_v_list:
#             ans = ans*10 + v
#         return -1 if ans > 2**31 -1 else ans
            

# sol = Solution()
# n = 12543
# res = sol.nextGreaterElement(n)
# print(res)

# from collections import deque
# class Solution:
#     def nextGreaterElement(self, n: int) -> int:
#         v_list = []
#         while n:
#             digit = n % 10
#             n = n //  10
#             v_list.append(digit)
#         v_list = v_list[::-1]
    
#         q = deque([(v_list[-1], len(v_list) - 1)])
#         left = len(v_list) - 1
#         while left >= 0 :
#             if q and v_list[left] < q[-1][0]:
#                 break
#             else:
#                 q.append((v_list[left], left))
#             left -= 1
            
#         if left < 0:
#             return -1
        
#         while q:
#             value, right = q.popleft() 
#             if value > v_list[left]:
#                 break
                
        
#         v_list[left], v_list[right] = v_list[right], v_list[left]
#         n_v_list = v_list[:left+ 1] + sorted(v_list[left+1:])
#         ans = 0
#         for v in n_v_list:
#             ans = ans*10 + v
#         return -1 if ans > 2**31 -1 else ans


### you only need to reverse the later half
from collections import deque
class Solution:
    def nextGreaterElement(self, n: int) -> int:
        v_list = [int(i) for i in list(str(n))]
        left = len(v_list) - 1
        while left >0:
            if v_list[left] > v_list[left - 1]:
                break
            left -= 1
        left -= 1
        if left < 0:
            return -1
        right = len(v_list) - 1
        while right >= 0:
            if v_list[right] > v_list[left]:
                break
            right -= 1
                
        v_list[left], v_list[right] = v_list[right], v_list[left]
        left, right = left +1, len(v_list) - 1
        while left < right:
            v_list[left], v_list[right] = v_list[right], v_list[left]
            left += 1
            right -=1
        ans = 0
        for v in v_list:
            ans = ans*10 + v
        return -1 if ans > 2**31 -1 else ans
            
            