from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token not in ["+", "-", "*", "/"]:
                stack.append(int(token))
            else: 
                b = stack.pop()
                a = stack.pop()

                if token == "+":
                    stack.append(a + b)
                elif token == "-":
                    stack.append(a - b)
                elif token == "*":
                    stack.append(a * b)
                else:
                    quotient = abs(a) // abs(b)
                    stack.append(-quotient if (a < 0) != (b < 0) else quotient)
        
        return stack[0]