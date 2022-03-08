from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = ['+', '-', '*', '/']
        self.current_pos = len(tokens) -1
        def posorder(tokens):
            if tokens[self.current_pos] not in operators:
                return int(tokens[self.current_pos])
            else:
                operator = tokens[self.current_pos]
                self.current_pos = self.current_pos -1
                left_operand = posorder(tokens)
                self.current_pos = self.current_pos -1
                right_operand = posorder(tokens)
                if operator == '+':
                    return left_operand + right_operand
                elif operator == '-':
                    return right_operand - left_operand
                elif operator == '*':
                    return right_operand * left_operand
                else:
                    return int(right_operand / left_operand)
        return posorder(tokens)

tokens = ["4","13","5","/","+"]
sol = Solution()
res = sol.evalRPN(tokens)
print(res)

        