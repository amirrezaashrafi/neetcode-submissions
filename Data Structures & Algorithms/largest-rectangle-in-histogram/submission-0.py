class Solution:
    def largestRectangleArea(self, heights):
        # Time complexity: O(n²) - two nested loops
        # Space complexity: O(1) - no extra space used
        
        largest = 0

        for i in range(len(heights)):
            # track minimum height as we expand right
            # so we dont recompute min() every iteration → O(1) instead of O(n)
            min_height = heights[i]

            for j in range(i, len(heights)):
                # update min height as the right boundary expands
                min_height = min(min_height, heights[j])

                # area = width * height
                # width = j - i + 1 (number of bars between i and j inclusive)
                # height = min_height (limited by the shortest bar in range)
                val = (j - i + 1) * min_height
                largest = max(largest, val)

        return largest