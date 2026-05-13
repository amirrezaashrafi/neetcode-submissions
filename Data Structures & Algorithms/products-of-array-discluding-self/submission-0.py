class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)
        output = list()
        for i in range(l):
            temp = 1
            for j in range(l):
                if i != j:
                    temp *= nums[j]
            output.append(temp)

        return output