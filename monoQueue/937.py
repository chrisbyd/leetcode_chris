from typing import List
from functools import cmp_to_key
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        def compare(a, b):
            a, b = a.split(" "), b.split(" ")
            if a[1:] == b[1:]:
                res =  int(a[0] > b[0])
                if res: return 1
                elif a[0] < b[0]:
                    return -1
                else:
                    return 0
            else:
                res = a[1:] > b[1:]
                if res: return 1
                else:
                    return -1
        digits, letters = [], []
        for log in logs:
            if ord(log.split(" ")[1][0]) >= 48 and ord(log.split(" ")[1][0]) <= 57:
                digits.append(log)
            else:
                letters.append(log)
        letters = sorted(letters, key = cmp_to_key(compare))
        return letters + digits
        