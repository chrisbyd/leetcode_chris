from typing import List
import math
import bisect
class Solution:
    def intToRoman(self, num: int) -> str:
        iToRoDict= {1: "I", 5: "V", 10: "X", 50: "L", 100: "C", 500: "D", 1000: "M"}
        iToRoDict1 = {4: 'IV', 9: 'IX', 40: 'XL', 90: 'XC', 400: 'CD', 900: 'CM'}
        numbers = [1, 5, 10, 50, 100, 500, 1000]
        num_to_list = []
        k = 1
        ans = ''
        while num != 0:
            digit = num % 10
            digit_to_store = k *  digit
            num_to_list.append(digit_to_store)
            k *= 10
            num = num // 10
        for i in range(len(num_to_list)-1 , -1 , -1):
            number = num_to_list[i]
            if number in iToRoDict1:
                ans += iToRoDict1[number]
            else:
                index = bisect.bisect_left(numbers, number)
                if index == 7:
                    index = index -1
                substract_number = numbers[index]
                while number != 0:
                    if number < substract_number:
                        index = index - 1
                        substract_number = numbers[index]
                    else:
                        number = number - substract_number
                        ans += iToRoDict[substract_number]
        return ans

sol = Solution()
num = 3999
res = sol.intToRoman(num)
print(res)

class Solution1:
    def intToRoman(self, num: int) -> str:
        d = {1000: "M", 900: "CM", 500: "D", 400: "CD", 100: "C", 90: "XC", 50: 'L', 40: "XL", 10: "X", 9: 'IX', 5: "V", 4: "IV", 1: "I"}
        ans = ''
        for k in d.keys():
            ans += (num // k) * d[k]
            num = num % k
        return ans


sol = Solution1()
num = 3999
res = sol.intToRoman(num)
print(res)




                
            



            



        