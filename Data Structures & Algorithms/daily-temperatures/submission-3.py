class Solution:
    def dailyTemperatures(self, temperatures):
        result = [0] * len(temperatures)
        stack = []

        for i, temperature in enumerate(temperatures):
            while stack and temperature > stack[-1][0]:
                _, j = stack.pop() 
                result[j] = i - j
            stack.append((temperature, i))
        
        return result