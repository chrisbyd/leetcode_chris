
from typing import List
import math
class Solution:
    def myAtoi(self, s: str) -> int:
        numbers = ['0','1','2','3','4','5','6','7','8','9']
        signs = ['-', '+']
        visited = False
        read_sign = False
        sign = ''
        int_string = ''
        for letter in s:
            if letter in signs and not read_sign and not visited:
                sign = letter
                read_sign = True
                visited = True
            elif letter in signs and read_sign:
                break
            elif letter in numbers and not visited:
                int_string += letter
                visited = True
            elif letter in numbers and visited:
                int_string += letter
            elif not visited and letter != ' ':
                return 0
            elif visited:
                break
        
        if int_string == "":
            return 0
        for i in range(len(int_string)):
            if int_string[i] != '0':
                break
        int_string = int_string[i:]
        if len(int_string) > 10:
            if sign == '-':
                return - int(math.pow(2,31))
            else:
                return int(math.pow(2,31) - 1)
        else:
            num = int(int_string)
          
            if sign == '-' and num >= int(math.pow(2,31)):
                return - int(math.pow(2,31))
            elif sign != '-' and num >= int(math.pow(2,31) -1):
                return  int(math.pow(2,31) -1 )
            elif sign == '-':
                return - num
            else:
                return num

sol = Solution()
test ="-5-"

res = sol.myAtoi(test)
print(res)


###