class Solution:
    def dailyTemperatures(self, temperatures):
        output = []
        for i in range(len(temperatures)):
            current_temp = temperatures[i]
            for j in range(i+1, len(temperatures)):
                if temperatures[j] > current_temp:
                    output.append(j - i)
                    break
            else:
                output.append(0)

        return output