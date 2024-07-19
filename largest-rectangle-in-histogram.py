class Solution:
    def largestRectangleArea(self, heights):
        s = [-1]
        area = 0

        for i in range(len(heights)):
            while s[-1] != -1 and heights[i] <= heights[s[-1]]:
                h = heights[s.pop()]
                w = i - s[-1] - 1
                area = max(area, h * w)
            s.append(i)
        
        while s[-1] != -1:
            h = heights[s.pop()]
            w = len(heights) - s[-1] - 1
            area = max(area, h * w)
        
        return area