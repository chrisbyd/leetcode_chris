from ast import operator
import collections
import sunau

from torch import sign

# class Solution:
#     def calculate(self, s: str) -> int:
#         queue = collections.deque(s)
#         print(queue)
#         def recursive(queue, stack):
#             operator = '+'
#             c_char = ''
#             print(queue)
#             while queue:
#                 print(stack)
#                 char = queue.popleft()
     
#                 if char.isdigit():
#                     c_char += char

#                 if char == '(':
#                     n_num = recursive(queue, ['('])
#                     print("The number is", n_num)
#                 elif char == ')':
#                     res = 0
#                     print("The stack is",stack)
#                     while stack[-1] != '(':
#                         res += stack.pop()
#                     return res
#                 if  (not char.isdigit() and char != " ") or len(queue) == 1:
#                     print("char", char, "c_char", c_char)
#                     if operator == '-':
#                         if char != '(':
#                             c_num = - int(c_char)
#                         else:
#                             c_num = n_num
#                         print("c number", c_num)
#                         stack.append(c_num)
#                         operator = char
#                         c_char = ''
#                     elif operator == '+':
#                         if char != '(':
#                             c_num =  int(c_char)
#                         else:
#                             c_num = n_num
#                         stack.append(c_num)
#                         operator = char
#                         c_char = ""
#                 ans = 0
#             while stack:
#                 ans += stack.pop()
#             return ans
        
#         return  recursive(queue, [])


# sol = Solution()

# s = " 2 - (1 + 2) "
# res = sol.calculate(s)
# print(res)


# 2 + （1 + （4 +5 +2））+ （6+8）
class Solution:
    def calculate(self, s: str) -> int:
        s += '-'
        stack = []
        sum = 0
        operator = '+'
        c_char = ''
        for idx, char in enumerate(s):
            if char.isdigit():
                c_char += char
            
            if char in ['+', '-'] or idx == len(s) -1:
                if operator == '+':
                    if c_char:
                        sum += int(c_char)
                    else:
                        sum += 0
                elif operator == '-':
                    if c_char:
                        sum -= int(c_char)
                    else:
                        sum -= 0
                operator = char
                c_char = ''
            elif char == '(':
                stack.append(sum)
                stack.append(operator)
                sum = 0
                operator = "+"
                c_char = ""
            elif char == ')':
                if operator == '+':
                    sum += int(c_char)
                elif operator == '-':
                    sum -= int(c_char)
                c_char = sum
                operator = stack.pop()
                sum = stack.pop()
        return sum 

sol = Solution()
            
s = "(1+(4+5+2)-3)+(6+8)"
s = "-2+ 1"
res = sol.calculate(s)
print(res)             
                 

                    
# the standard solution from youtube
class Solution1:
    def  calculate(self, s: str) -> int:
        operator = 1
        sum = 0
        stack = []
        c_char = ''
        for idx, char in enumerate(s):
            if char.isdigit() and idx +1 < len(s) and s[idx+1].isdigit():
                c_char += char
            elif char.isdigit() and (idx +1 == len(s) or not s[idx+1].isdigit()):
                c_char += char
                sum += operator * int(c_char)
                c_char = ''
            if char == '+':
                operator = 1
            elif char == '-':
                operator = -1
            elif char == '(':
                stack.append(sum)
                stack.append(operator)
                sum = 0
                operator = 1
            elif char == ')':
                sum = stack.pop() * sum
                sum += stack.pop()
        return sum


sol = Solution1()
            
s = "(1+(4+5+2)-3)+(6+8)"
#s = "-2+ 1"
res = sol.calculate(s)
print(res)         


             






            

        