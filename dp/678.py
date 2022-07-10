


## greedy algorithm and dynamic programming
# greddy solution is super hard so feel ok if you could not come up with this solution at the fist time
class Solution:
    def checkValidString(self, s: str) -> bool:
        minLeft = 0
        maxLeft = 0
        for char in s:
            if char == '(':
                minLeft += 1
                maxLeft += 1
            elif char == '*':
                if minLeft >= 1:
                    minLeft -= 1
                maxLeft += 1
            else:
                if maxLeft <= 0:
                    return False
                else:
                    if minLeft >= 1:
                        minLeft -= 1
                    maxLeft -= 1
        if minLeft == 0:
            return True
        return False

sol = Solution()
s = "(((((*(()((((*((**(((()()*)()()()*((((**)())*)*)))))))(())(()))())((*()()(((()((()*(())*(()**)()(())"
res = sol.checkValidString(s)
print(res)



        