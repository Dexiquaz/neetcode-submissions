class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area = 0
        for i in range(len(heights)):
            r = len(heights)-1

            while i<r:
                x = min(heights[i], heights[r])*(r-i)
                if x>area:
                    area = x
                if heights[i]<heights[r]:
                    i+=1
                r-=1

        return area
            
        