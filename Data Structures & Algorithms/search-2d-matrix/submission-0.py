class Solution:
    def searchMatrix(self, matrix, target):
        nums = []
        for row in matrix:
            nums += row
        
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (right + left) // 2

            if nums[mid] == target:
                return True
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return False