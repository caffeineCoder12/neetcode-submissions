class Solution:
    def maxArea(self, heights: List[int]) -> int:
        a = 0
        l,r = 0,len(heights)-1
        while l < r and r < len(heights):
            a = max(a,min(heights[l],heights[r])*abs(l-r))
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return a