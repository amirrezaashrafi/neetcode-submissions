class Solution:
    def evalRPN(self, tokens):
        stack = []
        for token in tokens:
            if token not in "+-/*":
                stack.append(int(token))
            else:
                val1, val2 = stack.pop(), stack.pop()
                if token == '+':
                    stack.append(val2 + val1)
                elif token == '-':
                    stack.append(val2 - val1)
                elif token == '*':
                    stack.append(val2 * val1)
                else:
                    stack.append(int(val2 / val1))
        
        return stack[-1]