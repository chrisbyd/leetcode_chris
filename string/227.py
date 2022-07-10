
# the rudimentary implementation which is not totally correct
from operator import index


class Solution:
    def calculate(self, s: str) -> int:
        s += '-'
        current_number = 0
        operator = ""
        c_char = ""
        stack = []
        for idx, char in enumerate(s):
            if char == " ":
                continue
            elif char.isdigit():
                c_char += char
            else:
                if operator in ["", "+"]:
                    current_number = int(c_char)
                    stack.append(current_number)
                elif operator == '-':
                    current_number = - int(c_char)
                    stack.append(current_number)
                elif operator == '*':
                    current_number = int(c_char)
                    current_number *= stack.pop()
                    stack.append(current_number)
                elif operator == '/':
                    current_number = int(c_char)
                    current_number = int(stack.pop() / current_number)
                    stack.append(current_number)
                operator = char
                c_char = ""
        ans = 0
        while stack:
            ans += stack.pop()
        return ans

sol = Solution()

s = "  3 + 5 / 2 "
res = sol.calculate(s)
# print(res)







                



class Solution:
    def calculate(self, s: str) -> int:
        current_number = 0
        operator = "+"
        c_char = ""
        stack = []
        for idx, char in enumerate(s):
            if char.isdigit():
                c_char += char

            if (not char.isdigit() and char != " ") or idx == len(s) -1 :
           

                if operator == '+':
                    current_number = int(c_char)
             
                    stack.append(current_number)
                elif operator == '-':
                    current_number = - int(c_char)
                    stack.append(current_number)
                elif operator == '*':
                    current_number = int(c_char)
                    current_number *= stack.pop()
                    stack.append(current_number)
                elif operator == '/':
                    current_number = int(c_char)
                    current_number = int(stack.pop() / current_number)
              
                    stack.append(current_number)
                operator = char
                c_char = ""
    
        ans = 0
        while stack:
            ans += stack.pop()
        return ans


sol = Solution()

s = "  3 + 5 / 2"
res = sol.calculate(s)
print(res)

