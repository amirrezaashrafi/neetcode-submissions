class Solution:
    def dailyTemperatures(self, temperatures):
        result = [0] * len(temperatures)
        stack = []

        for i, temperature in enumerate(temperatures):
            while stack and temperature > stack[-1][0]:
                result[stack[-1][1]] = i - stack[-1][1]
                stack.pop() 
            stack.append((temperature, i))
        
        return result