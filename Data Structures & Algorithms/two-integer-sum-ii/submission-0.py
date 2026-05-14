class Solution:
    def twoSum(self, numbers, target):
        l = len(numbers)

        for i in range(l):
            for j in range(i+1, l):
                if numbers[i] + numbers[j] == target:
                    return [i+1, j+1]