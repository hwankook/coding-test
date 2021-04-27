from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [-1]
        heights.append(0)
        area = 0
        for end in range(len(heights)):
            while heights[end] < heights[stack[-1]]:
                height = heights[stack.pop()]
                width = end - stack[-1] - 1
                area = max(area, width * height)
            stack.append(end)
        return area
