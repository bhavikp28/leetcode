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
            elif height[l] > height[r]:
                r -=1
            elif height[l] == height[r]:
                if height[l+1] >= height[r-1]:
                    l += 1
                else:
                    r -= 1
        return(maxarea)