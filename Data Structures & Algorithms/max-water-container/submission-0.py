# Time Complexity = O(n)
# Space Complexity = O(1)
class Solution:
    def maxArea(self, heights):
        left, right = 0, len(heights) - 1
        max_area = 0    

        while left < right:
            area = min(heights[right], heights[left]) * (right - left)
            max_area = max(max_area, area)

            if heights[right] > heights[left]:
                left += 1
            else:
                right -= 1

        return max_area     