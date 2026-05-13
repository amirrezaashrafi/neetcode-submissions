class Solution:
    def evalRPN(self, tokens):
        stack = []
        ops = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "*": lambda a, b: a * b,
            "/": lambda a, b: int(a / b) 
        }

        for token in tokens:
            if token in ops:
                val1, val2 = stack.pop(), stack.pop()
                stack.append(ops[token](val2, val1))
            else:
                stack.append(int(token))

        return stack[-1] 