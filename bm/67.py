class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        if len(a) >= len(b):
            first, second = a, b
        else:
            first, second =  b, a
        i, j = len(first) -1, len(second) - 1
        res = ""
        while i >= 0:
            if j >= 0: 
                cur =  (int(first[i]) + int(second[j]) + carry) % 2
                carry = (int(first[i]) + int(second[j]) + carry) // 2
                
            else:
                cur =  (int(first[i])  + carry) % 2
                carry = (int(first[i]) + carry) // 2
            i -= 1
            j -= 1
            res = str(cur) + res
        if carry == 1:
            res = '1' + res
        return res
            
                
        