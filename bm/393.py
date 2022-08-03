#### this is my dumb solution
from typing import List
####
# class Solution:
#     def validUtf8(self, data: List[int]) -> bool:
#         def get_binary_string(number):
#             return bin(number | (1 << 32))[-8:]
        
#         def get_bytes(binary_string):
#             if binary_string[0] == '0': return 1
#             if binary_string[:3] == '110': return 2
#             if binary_string[:4] == '1110': return 3
#             if binary_string[:5] == '11110': return 4
#             return 0
        
#         index, n  = 0, len(data)
#         while index < n:
#             b_string = get_binary_string(data[index])
#             b_n = get_bytes(b_string)
#             if not b_n: return False
#             while b_n != 1:
#                 index += 1
#                 if index >= n:
#                     return False
#                 n_b_string = get_binary_string(data[index])
#                 if n_b_string[:2] != '10': return False
#                 b_n -= 1
#             index += 1
#         return True
            
### another way is for string manipulation
class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        n_bytes = 0
        for num in data:
            bin_rep = format(num, '#010b')[-8:]

            if n_bytes == 0:
                for bit in bin_rep:
                    if bit == '0': break
                    n_bytes += 1
                    
                if n_bytes == 0: 
                    continue
                    
                if n_bytes == 1 or n_bytes > 4:
                    return False
            else:
                if bin_rep[:2] != '10': return False
            n_bytes -= 1
        return n_bytes == 0

data = [197, 130, 1]
sol = Solution()
res = sol.validUtf8(data)
print(res)
