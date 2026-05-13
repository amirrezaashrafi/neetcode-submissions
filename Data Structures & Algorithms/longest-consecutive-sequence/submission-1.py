class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0 
        look_up = set(nums)
        for i in range(len(nums)):
            num = nums[i]
            if (num - 1) not in look_up:
                temp = 0
                while num in look_up:
                    temp += 1
                    num += 1
                if temp > longest:
                    longest = temp

        return longest  