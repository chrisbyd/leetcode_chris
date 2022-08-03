class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        start, end = list(start), list(end)
        if len(start) != len(end): return False
        first, second = 0, 0
        while second != len(end):
            if start[first] == end[second]:
                first += 1
                second += 1
            else:
                if end[second] == 'R':
                    return False
                elif end[second] == 'X':
                    while first < len(end) and start[first] == 'R':
                        first += 1
                    if first == len(end) or start[first] == 'L' :
                        return False
                    else:
                        start[second], start[first] = start[first], start[second]
                        second += 1
                        first = second
                elif end[second] == 'L':
                    while first < len(start) and start[first] == 'X':
                        first += 1
                    if first == len(end) or start[first] != 'L'  :
                        return False
                    else:
                        start[second], start[first] = start[first], start[second]
                        second += 1
                        first = second
        return True
                        

#### with two pointer

class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        i, j = 0, 0
        n = len(start)
        while i < n or j < n:
            while i < n and start[i] == 'X':
                i += 1
            while j < n and end[j] == 'X':
                j += 1
            if i == n and j == n:
                return True
            elif i== n or j == n:
                return False
            elif start[i] != end[j]:
                return False
            
            if start[i] == 'R' and i > j:
                return False
            
            if start[i] == 'L' and i <j:
                return False
            
            i += 1
            j += 1
        return True
                
            
        
                        
        