class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        maxarea = 0
        while r > l:
            length = r-l
            h = min(height[r],height[l])
            area = length*h
            maxarea = max(maxarea,area)
            if height[l] < height[r]:
                l += 1
            else:
                r -=1
        return(maxarea)