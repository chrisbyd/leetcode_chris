from itertools import zip_longest
from typing import List

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'
        length = len(num1) + len(num2) 
        ans = [0 for i in range(length)]
        pos = length - 1
        for i in range(len(num1) -1, -1, -1):
            overflow = 0
            for j in range(len(num2)-1, -1, -1):
                res = (int(num1[i]) * int(num2[j]) + overflow) % 10
                overflow = (int(num1[i]) * int(num2[j]) + overflow) // 10
                temp = ans[pos - (len(num2) -1 - j)] + res
                overflow += temp //10
                ans[pos - (len(num2) -1 - j)] = temp % 10
                if j == 0:
                    ans[pos - (len(num2) -1 - j) -1] += overflow
            pos -= 1
        if ans[0] == 0:
            ans = ans[1:]
        res = ''
        for digi in ans:
            res += str(digi)
        return  res

sol = Solution()
num1 = "999"
num2 = "0"
res = sol.multiply(num1, num2)
print(res)
                



#Sum the products from all pairs of digits


class Solution1:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == '0':
            return '0'
        first_num = num1[::-1]
        second_num = num2[::-1]
        ans = []
        for index, digit2 in enumerate(second_num):
            ans.append(self.multiply_one_digit(digit2, index, first_num))
        print(ans)
        ans = self.sum_results(ans)
        return ''.join(str(digit) for digit in ans)
        

    def multiply_one_digit(self, digit2, num_zeros, first_number):
        current_result = [0] * num_zeros
        carry = 0
        for digit1 in first_number:
            multiplication = int(digit1) * int(digit2) + carry
            carry = multiplication // 10
            res = multiplication % 10
            current_result.append(res)
        if carry != 0:
            current_result.append(carry)
        return current_result


    def sum_results(self, results):
        answer = results.pop()
        for result in results:
            carry = 0
            new_answer = []
            for digit1, digit2 in zip_longest(answer, result, fillvalue= 0):
                sum_digit = digit1 + digit2 + carry
                carry = sum_digit // 10
                res = sum_digit % 10
                new_answer.append(res)
            if carry != 0:
                new_answer.append(carry)
            answer = new_answer
        return answer[::-1]
        
sol = Solution1()
num1 = "999"
num2 = "999"
res = sol.multiply(num1, num2)
print(res)
           


class Solution2:
    def multiply(self, num1: str, num2: str) -> str:
        pass
    
    
    
