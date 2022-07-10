from turtle import resetscreen
from typing import List
class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        def get_fn_bits(num):
            res= []
            divs = [128, 64, 32, 16, 8]
            for div in divs:
                if num // div == 0:
                    return res
                res.append(1)
                num = num - div
         
            return res
        flag = False
        count = 0 
        for i in range(len(data)):
            if len(get_fn_bits(data[i])) == 5:
                return False
            elif flag and len(get_fn_bits(data[i])) != 1:
                return False
            elif flag and len(get_fn_bits(data[i])) == 1:
                count -= 1
                if count == 0: 
                    flag = False
            elif not flag and len(get_fn_bits(data[i])) == 1:
                return False
            elif not flag and len(get_fn_bits(data[i])) > 1:
                count = sum(get_fn_bits(data[i])) - 1
                flag = True
        if count == 0:
            return True
        return False

sol = Solution()
data = [248,130,130,130]
res = sol.validUtf8(data=data)
print(res)        

# def get_fn_bits(num):
#         res= []
#         divs = [128, 64, 32, 16]
#         for div in divs:
#             if num // div == 0:
#                 return res
#             res.append(1)
#             num = num - div
        
#         return res
# for dat in data:
#     print(get_fn_bits(dat))




        