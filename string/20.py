from inspect import stack
from typing import List
import collections

class Solution:
    def isValid(self, s: str) -> bool:
        stack = collections.deque()
        dic = {'(':')', '[': ']', '{': '}'}
        for character in s:
           
            if character in ['(', '[', '{']:
                stack.append(character)
            elif len(stack) == 0:
                return False
            else:
                a = stack.pop()
                if character != dic[a]:
                    return False
        if len(stack) == 0:
            return True
        return False

sol = Solution()

s = "])"
res = sol.isValid(s)
print(res)


## for a dictionary 
#u could use get method to prevent key error
# it will return an empty if the key does not existss
class Solution1:
    def isValid(self, s: str) -> bool:
        stack = []
        dic = {')':'(', ']': '[', '}': '{'}
        for character in s:
            if stack and dic.get(character) == stack[-1]:
                stack.pop()
            else:
                stack.append(character)
        return not stack


sol = Solution1()

s = "([()]])"
res = sol.isValid(s)
print(res)
        



    





        